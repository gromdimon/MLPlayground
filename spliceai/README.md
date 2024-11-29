# SpliceAI C++ Reimplementation

![SpliceAI header](./assets/header.jpg)

SpliceAI is a deep learning-based tool designed for identifying splice sites in genomic sequences. This project is a C++ reimplementation of the original [SpliceAI](https://basespace.illumina.com/s/5u6ThOblecrh) project, which was implemented in Python using PyTorch. The reimplementation uses **LibTorch**, the official PyTorch C++ API, for defining and training the neural network models.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup](#setup)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Dataset Preparation](#dataset-preparation)
3. [Usage](#usage)
   - [Training the Model](#training-the-model)
   - [Testing the Model](#testing-the-model)
4. [Dataset Information](#dataset-information)
5. [Examples](#examples)

---

## Project Overview

SpliceAI is a state-of-the-art deep learning model that identifies splice sites in human genomic sequences. It uses convolutional neural networks with residual connections to predict acceptor and donor splice sites from DNA sequences.

This C++ implementation aims to provide a high-performance version of SpliceAI that can be integrated into other C++ applications or run independently.

Key features of this implementation:
- Implements the SpliceAI neural network variants (`80nt`, `400nt`, `2000nt`, `10000nt`).
- Compatible with Linux and macOS.
- Supports training, validation, and testing with HDF5 datasets.
- Uses **LibTorch** for neural network operations and **HDF5 C++ API** for data handling.

---

## Setup

### Prerequisites

1. **Linux or macOS**:
   - Ubuntu 20.04+ or macOS Big Sur+ recommended.
2. **C++ Compiler**:
   - GCC 8+ (Linux) or Clang (macOS).
3. **Libraries**:
   - [LibTorch](https://pytorch.org/cppdocs/installing.html) (PyTorch C++ API).
   - HDF5 library for reading and writing HDF5 files.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gromdimon/stronghold.git
   cd stronghold/spliceai
   ```

2. **Install Dependencies**:
   - **LibTorch**:
     Download and install LibTorch from the [official website](https://pytorch.org/get-started/locally/).
     ```bash
     wget https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-latest.zip
     unzip libtorch-shared-with-deps-latest.zip
     export TORCH_HOME=$(pwd)/libtorch
     ```

   - **HDF5 Library**:
     For Ubuntu:
     ```bash
     sudo apt-get install libhdf5-dev
     ```
     For macOS (using Homebrew):
     ```bash
     brew install hdf5
     ```

3. **Build the Project**:
   - Use CMake to build the project:
     ```bash
     mkdir build
     cd build
     cmake -DCMAKE_PREFIX_PATH=$TORCH_HOME ..
     make
     ```

---

## Dataset Preparation

1. **Download the SpliceAI Train Code**:
   - Download the SpliceAI training code directory from [Illumina BaseSpace](https://basespace.illumina.com/s/5u6ThOblecrh).
   - Unzip it into the `spliceai_train_code` directory:
     ```bash
     mkdir spliceai_train_code
     unzip path/to/spliceai_train_code.zip -d spliceai_train_code
     ```

2. **Download the Human Reference Genome**:
   - Download the `hg19` reference genome into the `spliceai_train_code/reference` directory.

3. **Generate Training and Test Sets**:
   - Navigate to the `spliceai_train_code/Canonical` directory:
     ```bash
     cd spliceai_train_code/Canonical
     ```

   - Configure the `CL_max` variable in `constants.py` to the desired sequence length (e.g., `80`, `400`, `2000`, or `10000`).

   - Run the following commands to generate train/test datasets:
     ```bash
     chmod 755 grab_sequence.sh
     ./grab_sequence.sh

     # Requires Python 2.7 with numpy, h5py, scikit-learn installed
     python create_datafile.py train all  # ~4 minutes
     python create_datafile.py test 0    # ~1 minute

     python create_dataset.py train all  # ~11 minutes
     python create_dataset.py test 0     # ~1 minute
     ```

   - This will create:
     - `dataset_train_all.h5` (~5.4 GB)
     - `dataset_test_0.h5` (~0.5 GB)

---

## Usage

### Training the Model

To train the SpliceAI model, use the following command:
```bash
./train --model 80nt --output model.pt --train-h5 spliceai_train_code/Canonical/dataset_train_all.h5 --test-h5 spliceai_train_code/Canonical/dataset_test_0.h5 --epochs 10 --batch-size 18 --learning-rate 0.001 --seed 42
```

### Testing the Model

To test the trained model on a test dataset:
```bash
./train --model 80nt --test-only --test-h5 spliceai_train_code/Canonical/dataset_test_0.h5 --pretrained model.pt
```

---

## Dataset Information

The dataset for this project consists of genomic sequences and corresponding splice site labels.

- **Input**: DNA sequences encoded as a one-hot matrix (shape: `(batch_size, 4, sequence_length)`).
- **Output**: Labels indicating the likelihood of a position being an acceptor or donor splice site.

### Files:

- **Training Dataset**:
  - File: `dataset_train_all.h5`
  - Size: ~5.4 GB
- **Testing Dataset**:
  - File: `dataset_test_0.h5`
  - Size: ~0.5 GB

### Data Format:

- **HDF5 Structure**:
  - `X{shard_idx}`: Input DNA sequences (shape: `(num_samples, sequence_length, 4)`).
  - `Y{shard_idx}`: Labels (shape: `(num_samples, sequence_length, 3)`).

---

## Examples

### Training Example

Training a `400nt` model with default parameters:
```bash
./train --model 400nt --output spliceai_400nt.pt --train-h5 spliceai_train_code/Canonical/dataset_train_all.h5 --test-h5 spliceai_train_code/Canonical/dataset_test_0.h5 --epochs 15
```

### Testing Example

Evaluating the trained model:
```bash
./train --model 400nt --test-only --test-h5 spliceai_train_code/Canonical/dataset_test_0.h5 --pretrained spliceai_400nt.pt
```

