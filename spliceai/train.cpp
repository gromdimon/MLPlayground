#include <torch/torch.h>
#include <iostream>
#include <vector>
#include <random>
#include "spliceai.h"
#include "data_loader.h"
#include "H5Cpp.h"

void seed_everything(int seed) {
    torch::manual_seed(seed);
    torch::cuda::manual_seed(seed);
    torch::cuda::manual_seed_all(seed);
    std::srand(seed);
}

std::vector<int> shuffle_indices(int num_indices) {
    std::vector<int> indices(num_indices);
    std::iota(indices.begin(), indices.end(), 0);
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(indices.begin(), indices.end(), g);
    return indices;
}

void train(
    std::shared_ptr<torch::nn::Module> model,
    H5::H5File& h5f,
    std::vector<int>& train_shard_idxs,
    int batch_size,
    torch::optim::Optimizer& optimizer,
    torch::nn::CrossEntropyLoss& criterion
) {
    model->train();
    std::vector<torch::Tensor> running_output, running_label;
    int batch_idx = 0;

    // Shuffle the shard indices
    auto shuffled_shard_idxs = train_shard_idxs;
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(shuffled_shard_idxs.begin(), shuffled_shard_idxs.end(), g);

    for (size_t i = 0; i < shuffled_shard_idxs.size(); ++i) {
        int shard_idx = shuffled_shard_idxs[i];

        // Load data from HDF5
        std::string dataset_x_name = "X" + std::to_string(shard_idx);
        std::string dataset_y_name = "Y" + std::to_string(shard_idx);

        // Similar to data_loader.cpp, read datasets X and Y
        // Create a DataLoader for this shard
        // For brevity, let's assume we have a function that creates a DataLoader from HDF5 datasets

        HDF5Dataset shard_dataset(h5f.getFileName(), shard_idx);
        auto data_loader = torch::data::make_data_loader<torch::data::samplers::RandomSampler>(
            std::move(shard_dataset),
            batch_size
        );

        // Iterate over batches
        for (auto& batch : *data_loader) {
            auto X = batch.data.to(torch::kCUDA);
            auto Y = batch.target.to(torch::kCUDA);

            optimizer.zero_grad();
            auto output = model->forward(X);

            // Reshape output and targets
            auto output_reshaped = output.view({-1, 3});
            auto Y_argmax = std::get<1>(Y.max(2));
            auto Y_reshaped = Y_argmax.view({-1});

            auto loss = criterion(output_reshaped, Y_reshaped);
            loss.backward();
            optimizer.step();

            running_output.push_back(output.detach().cpu());
            running_label.push_back(Y.detach().cpu());

            // Periodically compute metrics and log
            if (batch_idx % 1000 == 0) {
                // Compute metrics
                // For brevity, metrics computation is omitted
                // Clear running outputs and labels
                running_output.clear();
                running_label.clear();

                // Print training progress
                std::cout << "Batch " << batch_idx << ", Loss: " << loss.item<double>() << std::endl;
            }

            ++batch_idx;
        }
    }
}

double top_k_accuracy(torch::Tensor pred_probs, torch::Tensor labels) {
    // Flatten tensors
    pred_probs = pred_probs.view(-1);
    labels = labels.view(-1);

    int k = labels.eq(1.0).sum().item<int>();

    auto topk = std::get<1>(pred_probs.topk(k));
    auto correct = labels.index_select(0, topk).eq(1.0);

    return correct.to(torch::kFloat32).mean().item<double>();
}

void validate(
    std::shared_ptr<torch::nn::Module> model,
    H5::H5File& h5f,
    std::vector<int>& val_shard_idxs,
    int batch_size,
    torch::nn::CrossEntropyLoss& criterion
) {
    model->eval();
    // Implement the validation loop
}

void test(
    std::shared_ptr<torch::nn::Module> model,
    H5::H5File& h5f,
    std::vector<int>& test_shard_idxs,
    int batch_size,
    torch::nn::CrossEntropyLoss& criterion
) {
    model->eval();
    // Implement the testing loop
}

int main(int argc, const char* argv[]) {
    // Parse command-line arguments
    std::string model_name = "80nt"; // For example
    std::string output_path = "model.pt";
    std::string train_h5_path = "dataset_train_all.h5";
    std::string test_h5_path = "dataset_test_all.h5";
    int epochs = 10;
    int batch_size = 18;
    double learning_rate = 1e-3;
    int seed = 42;

    seed_everything(seed);

    // Open HDF5 files
    H5::H5File train_h5f(train_h5_path, H5F_ACC_RDONLY);
    H5::H5File test_h5f(test_h5_path, H5F_ACC_RDONLY);

    // Determine the number of shards
    int num_train_shards = train_h5f.getNumObjs() / 2;
    auto shard_idxs = shuffle_indices(num_train_shards);
    int train_size = static_cast<int>(0.9 * num_train_shards);
    std::vector<int> train_shard_idxs(shard_idxs.begin(), shard_idxs.begin() + train_size);
    std::vector<int> val_shard_idxs(shard_idxs.begin() + train_size, shard_idxs.end());

    int num_test_shards = test_h5f.getNumObjs() / 2;
    std::vector<int> test_shard_idxs(num_test_shards);
    std::iota(test_shard_idxs.begin(), test_shard_idxs.end(), 0);

    // Initialize the model
    std::shared_ptr<torch::nn::Module> model;
    if (model_name == "80nt") {
        model = std::make_shared<SpliceAI_80nt>();
    }
    // Add other model variants as needed

    model->to(torch::kCUDA);

    // Define loss function and optimizer
    torch::nn::CrossEntropyLoss criterion;
    torch::optim::Adam optimizer(model->parameters(), torch::optim::AdamOptions(learning_rate));

    // Training loop
    for (int epoch = 0; epoch < epochs; ++epoch) {
        std::cout << "Epoch " << (epoch + 1) << "/" << epochs << std::endl;
        train(model, train_h5f, train_shard_idxs, batch_size, optimizer, criterion);
        validate(model, train_h5f, val_shard_idxs, batch_size, criterion);
        test(model, test_h5f, test_shard_idxs, batch_size, criterion);
    }

    // Save the model
    torch::save(model, output_path);

    return 0;
}