cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(SpliceAI_Cpp)

find_package(Torch REQUIRED)
find_package(HDF5 REQUIRED COMPONENTS CXX)

set(CMAKE_CXX_STANDARD 14)

add_executable(train train.cpp data_loader.cpp spliceai.cpp)
target_link_libraries(train "${TORCH_LIBRARIES}" "${HDF5_LIBRARIES}")
set_property(TARGET train PROPERTY CXX_STANDARD 14)