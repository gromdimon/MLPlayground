#ifndef DATA_LOADER_H
#define DATA_LOADER_H

#include <torch/torch.h>
#include <string>
#include <vector>
#include "H5Cpp.h"

class HDF5Dataset : public torch::data::Dataset<HDF5Dataset> {
public:
    HDF5Dataset(const std::string& file_path, int shard_idx);

    torch::data::Example<> get(size_t index) override;
    torch::optional<size_t> size() const override;

private:
    std::vector<torch::Tensor> data_;
    std::vector<torch::Tensor> targets_;
};

#endif // DATA_LOADER_H