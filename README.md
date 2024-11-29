# Stronghold: Various ML Prohjects + Algo Implementations

![Abstract Header. Generated with DALL-E 3](assets/header.png)


## Introduction

This repository contains various machine learning projects and algorithm implementations, which I 
create for fun and learning. This is just a hub for my personal interests and experiments.

## Contents of the repo

The repo has a folder "algo" for various algorithms. Other folders are dedicated to different projects.

> [!NOTE]
> Each project within this repository may have additional setup or instructions. Please refer to the 
> `README.md` file within each project's directory for more specialized guidance.


### Projects Included:
- SpliceAI: A reimplementation of SpliceAI algorithm based on [paper](https://doi.org/10.1016/j.cell.2018.12.015)
- Mikrograd: A minimal autograd engine based on [micrograd](https://github.com/karpathy/micrograd) by `Andrej Karpathy`
- Makemore: A tool for generating synthetic data. Based on the [makemore](https://github.com/karpathy/makemore/tree/master) by `Andrej Karpathy`
- RuPoemGPT: A character-level language model trained on a collection of russian poems. Based on the [nanoGPT](https://github.com/karpathy/nanoGPT) by `Andrej Karpathy`

  **Also here are some older projects, which were not included into this repository:**
- [Glycoprotein prediction with AlphaFold2](https://github.com/gromdimon/AlphaFold_Glycoprotein)
- [Analysis of Long COVID Symptoms using BERT and Twitter Data](https://github.com/gromdimon/LongCovid)
- [Compound bioactivity prediction](https://github.com/gromdimon/Bioactivity_prediction_project)
- [General Machine Learning Techniques practice](https://github.com/gromdimon/Training--Projects)


## Tech

Note, that this repo has shared python environment, which is defined in `Pipfile`. The reason is 
simple - all projects are simple enough to have only standard dependencies with no conflicts.

> [!NOTE]
> Some algorithms are implemented in different languages, e.g. C++. 
> The notes how to run them are in the corresponding folders.


## Getting Started

These instructions will help you set up the python env for the repo, if you want to run the code 
locally. I'll use `pyenv` and `pipenv` for this, but you can use any other tools you like.

### Prerequisites

Ensure you have `pyenv` and `pipenv` installed on your system. If not, follow these steps:

- Install `pyenv`:
  ```
  curl https://pyenv.run | bash
  ```

- Install `pipenv`:
  ```
  pip install pipenv
  ```

### Installation

Follow these steps to get your development environment running:

1. Clone the repository:
   ```
   git clone https://github.com/gromdimon/stronghold.git
   ```

2. Navigate to the project directory:
   ```
   cd stronghold
   ```

3. Set the local Python version using `pyenv`:
   ```
   pyenv install 3.12
   ```

4. Install `pipenv` for the local Python version:
   ```
   pip install --user pipenv
   ```

5. Install dependencies using `pipenv`:
   ```
   pipenv install
   ```

6. Activate the `pipenv` environment:
   ```
   pipenv shell
   ```

## License

Distributed under the MIT License, so you can use it for any purpose `:)`
