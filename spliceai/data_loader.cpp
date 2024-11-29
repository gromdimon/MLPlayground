#include "data_loader.h"
#include <iostream>

HDF5Dataset::HDF5Dataset(const std::string& file_path, int shard_idx) {
    try {
        H5::H5File file(file_path, H5F_ACC_RDONLY);

        // Read dataset X
        std::string dataset_x_name = "X" + std::to_string(shard_idx);
        H5::DataSet dataset_x = file.openDataSet(dataset_x_name);
        H5::DataSpace dataspace_x = dataset_x.getSpace();

        // Get dimensions
        hsize_t dims_x[3];
        dataspace_x.getSimpleExtentDims(dims_x, NULL);

        // Read data into buffer
        std::vector<float> x_data(dims_x[0] * dims_x[1] * dims_x[2]);
        dataset_x.read(x_data.data(), H5::PredType::NATIVE_FLOAT);

        // Convert to Tensor and transpose to match PyTorch dimensions
        auto x_tensor = torch::from_blob(x_data.data(), {dims_x[0], dims_x[1], dims_x[2]}, torch::kFloat32).clone();
        x_tensor = x_tensor.permute({0, 2, 1}); // From (N, L, C) to (N, C, L)

        // Read dataset Y
        std::string dataset_y_name = "Y" + std::to_string(shard_idx);
        H5::DataSet dataset_y = file.openDataSet(dataset_y_name);
        H5::DataSpace dataspace_y = dataset_y.getSpace();

        // Get dimensions
        hsize_t dims_y[3];
        dataspace_y.getSimpleExtentDims(dims_y, NULL);

        // Read data into buffer
        std::vector<float> y_data(dims_y[0] * dims_y[1] * dims_y[2]);
        dataset_y.read(y_data.data(), H5::PredType::NATIVE_FLOAT);

        // Convert to Tensor
        auto y_tensor = torch::from_blob(y_data.data(), {dims_y[1], dims_y[2]}, torch::kFloat32).clone();

        // Store data and targets
        data_.push_back(x_tensor);
        targets_.push_back(y_tensor);

    } catch (H5::FileIException& error) {
        error.printErrorStack();
    } catch (H5::DataSetIException& error) {
        error.printErrorStack();
    } catch (H5::DataSpaceIException& error) {
        error.printErrorStack();
    }
}

torch::data::Example<> HDF5Dataset::get(size_t index) {
    return {data_[index], targets_[index]};
}

torch::optional<size_t> HDF5Dataset::size() const {
    return data_.size();
}