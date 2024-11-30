#include "spliceai.h"
#include <iostream>

ResidualImpl::ResidualImpl(torch::nn::Sequential fn) : fn_(fn) {
    register_module("fn", fn_);
}

torch::Tensor ResidualImpl::forward(torch::Tensor x) {
    return x + fn_->forward(x);
}

Residual ResidualBlock(int64_t in_channels, int64_t out_channels, int64_t kernel_size, int64_t dilation) {
    return Residual(
        torch::nn::Sequential(
            torch::nn::BatchNorm1d(torch::nn::BatchNorm1dOptions(in_channels)),
            torch::nn::ReLU(),
            torch::nn::Conv1d(torch::nn::Conv1dOptions(in_channels, out_channels, kernel_size)
                              .dilation(dilation).padding(torch::kSame)),
            torch::nn::BatchNorm1d(torch::nn::BatchNorm1dOptions(out_channels)),
            torch::nn::ReLU(),
            torch::nn::Conv1d(torch::nn::Conv1dOptions(out_channels, out_channels, kernel_size)
                              .dilation(dilation).padding(torch::kSame))
        )
    );
}

SpliceAI_80ntImpl::SpliceAI_80ntImpl() {
    // Initialize layers
    conv1 = register_module("conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(4, 32, 1)
                                                       .dilation(1).padding(torch::kSame)));
    res_conv1 = register_module("res_conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block1
    block1 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1).dilation(1).padding(torch::kSame))
    );
    register_module("block1", block1);

    conv_last = register_module("conv_last", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 3, 1)
                                                               .dilation(1).padding(torch::kSame)));
}

torch::Tensor SpliceAI_80ntImpl::forward(torch::Tensor x) {
    x = conv1->forward(x);
    auto detour = res_conv1->forward(x);
    x = detour + block1->forward(x);
    x = conv_last->forward(x);

    // Rearrange x from (N, C, L) to (N, L, C) and slice
    x = x.permute({0, 2, 1});
    x = x.slice(1, 40, 5000 + 40);

    return x;
}

SpliceAI_400ntImpl::SpliceAI_400ntImpl() {
    // Initialize layers
    conv1 = register_module("conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(4, 32, 1)
                                                       .dilation(1).padding(torch::kSame)));
    res_conv1 = register_module("res_conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block1
    block1 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1)
    );
    register_module("block1", block1);

    // Residual connection after block1
    res_conv2 = register_module("res_conv2", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block2
    block2 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1).dilation(1).padding(torch::kSame))
    );
    register_module("block2", block2);

    // Final output layer
    conv_last = register_module("conv_last", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 3, 1)
                                                               .dilation(1).padding(torch::kSame)));
}

torch::Tensor SpliceAI_400ntImpl::forward(torch::Tensor x) {
    x = conv1->forward(x);
    auto detour = res_conv1->forward(x);

    x = block1->forward(x);
    detour += res_conv2->forward(x);

    x = block2->forward(x) + detour;
    x = conv_last->forward(x);

    // Rearrange tensor from (N, C, L) to (N, L, C) and slice
    x = x.permute({0, 2, 1});
    x = x.slice(1, 200, 5000 + 200);

    return x;
}

SpliceAI_2kImpl::SpliceAI_2kImpl() {
    // Initialize layers
    conv1 = register_module("conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(4, 32, 1)
                                                       .dilation(1).padding(torch::kSame)));
    res_conv1 = register_module("res_conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block1
    block1 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1)
    );
    register_module("block1", block1);

    // Residual connection after block1
    res_conv2 = register_module("res_conv2", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block2
    block2 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4)
    );
    register_module("block2", block2);

    // Residual connection after block2
    res_conv3 = register_module("res_conv3", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block3
    block3 = torch::nn::Sequential(
        ResidualBlock(32, 32, 21, 10),
        ResidualBlock(32, 32, 21, 10),
        ResidualBlock(32, 32, 21, 10),
        ResidualBlock(32, 32, 21, 10),
        torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1).dilation(1).padding(torch::kSame))
    );
    register_module("block3", block3);

    // Final output layer
    conv_last = register_module("conv_last", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 3, 1)
                                                               .dilation(1).padding(torch::kSame)));
}

torch::Tensor SpliceAI_2kImpl::forward(torch::Tensor x) {
    x = conv1->forward(x);
    auto detour = res_conv1->forward(x);

    x = block1->forward(x);
    detour += res_conv2->forward(x);

    x = block2->forward(x);
    detour += res_conv3->forward(x);

    x = block3->forward(x) + detour;
    x = conv_last->forward(x);

    // Rearrange tensor from (N, C, L) to (N, L, C) and slice
    x = x.permute({0, 2, 1});
    x = x.slice(1, 1000, 5000 + 1000);

    return x;
}

SpliceAI_10kImpl::SpliceAI_10kImpl() {
    // Initialize layers
    conv1 = register_module("conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(4, 32, 1)
                                                       .dilation(1).padding(torch::kSame)));
    res_conv1 = register_module("res_conv1", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block1
    block1 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1),
        ResidualBlock(32, 32, 11, 1)
    );
    register_module("block1", block1);

    // Residual connection after block1
    res_conv2 = register_module("res_conv2", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block2
    block2 = torch::nn::Sequential(
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4),
        ResidualBlock(32, 32, 11, 4)
    );
    register_module("block2", block2);

    // Residual connection after block2
    res_conv3 = register_module("res_conv3", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block3
    block3 = torch::nn::Sequential(
        ResidualBlock(32, 32, 21, 10),
        ResidualBlock(32, 32, 21, 10),
        ResidualBlock(32, 32, 21, 10),
        ResidualBlock(32, 32, 21, 10)
    );
    register_module("block3", block3);

    // Residual connection after block3
    res_conv4 = register_module("res_conv4", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 32, 1)
                                                               .dilation(1).padding(torch::kSame)));

    // Build block4
    block4 = torch::nn::Sequential(
        ResidualBlock(32, 32, 41, 25),
        ResidualBlock(32, 32, 41, 25),
        ResidualBlock(32, 32, 41, 25),
        ResidualBlock(32, 32, 41, 25)
    );
    register_module("block4", block4);

    // Final output layer
    conv_last = register_module("conv_last", torch::nn::Conv1d(torch::nn::Conv1dOptions(32, 3, 1)
                                                               .dilation(1).padding(torch::kSame)));
}

torch::Tensor SpliceAI_10kImpl::forward(torch::Tensor x) {
    x = conv1->forward(x);
    auto detour = res_conv1->forward(x);

    x = block1->forward(x);
    detour += res_conv2->forward(x);

    x = block2->forward(x);
    detour += res_conv3->forward(x);

    x = block3->forward(x);
    detour += res_conv4->forward(x);

    x = block4->forward(x) + detour;
    x = conv_last->forward(x);

    // Rearrange tensor from (N, C, L) to (N, L, C) and slice
    x = x.permute({0, 2, 1});
    x = x.slice(1, 5000, 5000 + 5000);

    return x;
}
