cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(SpliceAI_Cpp)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add libtorch
find_package(Torch REQUIRED)

# Add HDF5
set(HDF5_ROOT "/opt/homebrew")
set(HDF5_INCLUDE_DIRS "${HDF5_ROOT}/include")
set(HDF5_LIBRARIES "${HDF5_ROOT}/lib/libhdf5.dylib")

# Add include directories
include_directories(${HDF5_INCLUDE_DIRS})
include_directories(${TORCH_INCLUDE_DIRS})

# Add executable and link libraries
add_executable(train train.cpp data_loader.cpp spliceai.cpp)
target_link_libraries(train "${TORCH_LIBRARIES}" "${HDF5_LIBRARIES}")
set_property(TARGET train PROPERTY CXX_STANDARD 17)

# Optional: Print HDF5 paths for debugging
message(STATUS "HDF5 Include: ${HDF5_INCLUDE_DIRS}")
message(STATUS "HDF5 Libraries: ${HDF5_LIBRARIES}")