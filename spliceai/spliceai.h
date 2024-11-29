#ifndef SPLICEAI_H
#define SPLICEAI_H

#include <torch/torch.h>
#include <string>

struct ResidualImpl : torch::nn::Module {
    ResidualImpl(torch::nn::Sequential fn);

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Sequential fn_;
};
TORCH_MODULE(Residual);

torch::nn::Sequential ResidualBlock(int64_t in_channels, int64_t out_channels, int64_t kernel_size, int64_t dilation);

struct SpliceAI_80ntImpl : torch::nn::Module {
    SpliceAI_80ntImpl();

    torch::Tensor forward(torch::Tensor x);

private:
    torch::nn::Conv1d conv1{nullptr}, res_conv1{nullptr}, conv_last{nullptr};
    torch::nn::Sequential block1;
};
TORCH_MODULE(SpliceAI_80nt);

// Similarly, define SpliceAI_400nt, SpliceAI_2k, and SpliceAI_10k

#endif // SPLICEAI_H