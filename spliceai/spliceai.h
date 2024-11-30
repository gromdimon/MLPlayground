#ifndef SPLICEAI_H
#define SPLICEAI_H

#include <torch/torch.h>
#include <string>

// Residual block class to add skip connections
struct ResidualImpl : torch::nn::Module {
    ResidualImpl(torch::nn::Sequential fn);

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Sequential fn_;
};
TORCH_MODULE(Residual);

// Function to create a residual block with BatchNorm, ReLU, and Conv1D layers
Residual ResidualBlock(int64_t in_channels, int64_t out_channels, int64_t kernel_size, int64_t dilation);

// SpliceAI_80nt Model
struct SpliceAI_80ntImpl : torch::nn::Module {
    SpliceAI_80ntImpl();

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Conv1d conv1{nullptr}, res_conv1{nullptr}, conv_last{nullptr};
    torch::nn::Sequential block1;
};
TORCH_MODULE(SpliceAI_80nt);

// SpliceAI_400nt Model
struct SpliceAI_400ntImpl : torch::nn::Module {
    SpliceAI_400ntImpl();

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Conv1d conv1{nullptr}, res_conv1{nullptr}, conv_last{nullptr};
    torch::nn::Conv1d res_conv2{nullptr};
    torch::nn::Sequential block1, block2;
};
TORCH_MODULE(SpliceAI_400nt);

// SpliceAI_2k Model
struct SpliceAI_2kImpl : torch::nn::Module {
    SpliceAI_2kImpl();

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Conv1d conv1{nullptr}, res_conv1{nullptr}, conv_last{nullptr};
    torch::nn::Conv1d res_conv2{nullptr}, res_conv3{nullptr};
    torch::nn::Sequential block1, block2, block3;
};
TORCH_MODULE(SpliceAI_2k);

// SpliceAI_10k Model
struct SpliceAI_10kImpl : torch::nn::Module {
    SpliceAI_10kImpl();

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Conv1d conv1{nullptr}, res_conv1{nullptr}, conv_last{nullptr};
    torch::nn::Conv1d res_conv2{nullptr}, res_conv3{nullptr}, res_conv4{nullptr};
    torch::nn::Sequential block1, block2, block3, block4;
};
TORCH_MODULE(SpliceAI_10k);

#endif // SPLICEAI_H