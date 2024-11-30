#include <torch/torch.h>
#include <torch/data/dataloader.h>
#include <iostream>
#include <vector>
#include <random>
#include "spliceai.h"
#include "data_loader.h"

// Function to calculate top-k accuracy
float top_k_accuracy(torch::Tensor pred_probs, torch::Tensor labels) {
    pred_probs = pred_probs.flatten();
    labels = labels.flatten();

    int k = labels.sum().item<int>();  // Number of positive labels
    auto top_k_indices = std::get<1>(pred_probs.topk(k));
    auto correct = labels.index_select(0, top_k_indices).eq(1).to(torch::kFloat32);

    return correct.mean().item<float>();
}

// Training function
void train(std::shared_ptr<torch::nn::Module> model, HDF5Dataset& dataset,
           const std::vector<int>& shard_idxs, int batch_size,
           torch::optim::Optimizer& optimizer, torch::nn::CrossEntropyLoss& criterion) {
    model->train();
    torch::data::DataLoaderOptions options(batch_size);
    torch::data::DataLoader<HDF5Dataset> loader(dataset, options);

    for (const auto& batch : loader) {
        auto x = batch.data.to(torch::kCUDA);
        auto y = batch.target.to(torch::kCUDA);

        optimizer.zero_grad();
        auto output = model->forward(x);
        auto loss = criterion(output.view({-1, 3}), y.argmax(1).view(-1));
        loss.backward();
        optimizer.step();

        std::cout << "Train Loss: " << loss.item<float>() << std::endl;
    }
}

// Validation function
float validate(std::shared_ptr<torch::nn::Module> model, HDF5Dataset& dataset,
               const std::vector<int>& shard_idxs, int batch_size,
               torch::nn::CrossEntropyLoss& criterion) {
    model->eval();
    torch::NoGradGuard no_grad;

    torch::Tensor all_outputs, all_labels;
    for (int shard_idx : shard_idxs) {
        HDF5Dataset shard_dataset(dataset.get_path(), shard_idx);
        torch::data::DataLoaderOptions options(batch_size);
        torch::data::DataLoader<HDF5Dataset> loader(shard_dataset, options);

        for (const auto& batch : loader) {
            auto x = batch.data.to(torch::kCUDA);
            auto y = batch.target.to(torch::kCUDA);
            auto output = model->forward(x);

            all_outputs = all_outputs.defined() ? torch::cat({all_outputs, output}) : output;
            all_labels = all_labels.defined() ? torch::cat({all_labels, y}) : y;
        }
    }

    auto output_probs = torch::softmax(all_outputs, -1);
    auto loss = criterion(output_probs.view({-1, 3}), all_labels.argmax(1).view(-1));

    auto top_k_acc = top_k_accuracy(output_probs, all_labels);
    std::cout << "Validation Loss: " << loss.item<float>() << " Top-k Accuracy: " << top_k_acc << std::endl;

    return loss.item<float>();
}

// Main function
int main(int argc, char* argv[]) {
    // Argument parsing (basic implementation)
    if (argc < 6) {
        std::cerr << "Usage: " << argv[0]
                  << " --model <80nt|400nt|2k|10k> --train-h5 <train.h5> --test-h5 <test.h5> "
                  << "--epochs <num_epochs> --batch-size <batch_size> --lr <learning_rate>" << std::endl;
        return 1;
    }

    std::string model_name = argv[2];
    std::string train_h5 = argv[4];
    std::string test_h5 = argv[6];
    int epochs = std::stoi(argv[8]);
    int batch_size = std::stoi(argv[10]);
    float learning_rate = std::stof(argv[12]);

    // Select model
    std::shared_ptr<torch::nn::Module> model;
    if (model_name == "80nt") {
        model = std::make_shared<SpliceAI_80nt>();
    } else if (model_name == "400nt") {
        model = std::make_shared<SpliceAI_400nt>();
    } else if (model_name == "2k") {
        model = std::make_shared<SpliceAI_2k>();
    } else if (model_name == "10k") {
        model = std::make_shared<SpliceAI_10k>();
    } else {
        std::cerr << "Unknown model: " << model_name << std::endl;
        return 1;
    }
    model->to(torch::kCUDA);

    // Load datasets
    HDF5Dataset train_dataset(train_h5, 0);  // Using shard 0 for now
    HDF5Dataset test_dataset(test_h5, 0);

    // Create optimizer and loss function
    auto optimizer = torch::optim::Adam(model->parameters(), torch::optim::AdamOptions(learning_rate));
    torch::nn::CrossEntropyLoss criterion;

    // Training loop
    for (int epoch = 0; epoch < epochs; ++epoch) {
        std::cout << "Epoch " << (epoch + 1) << "/" << epochs << std::endl;
        train(model, train_dataset, {0}, batch_size, optimizer, criterion);  // Replace {0} with shard indices
        validate(model, test_dataset, {0}, batch_size, criterion);           // Replace {0} with shard indices
    }

    // Save the model
    torch::save(model, "spliceai_model.pt");

    return 0;
}