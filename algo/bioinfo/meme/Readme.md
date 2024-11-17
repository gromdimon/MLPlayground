# MEME Algorithm Implementation

## Date
25.11.2023

## Description

This script implements the MEME (Multiple EM for Motif Elicitation) algorithm, a widely used method in bioinformatics for finding motifs - repeated, conserved patterns - within sets of DNA or protein sequences. 

The MEME algorithm uses an Expectation-Maximization (EM) approach to identify these motifs. It starts with a randomly initialized model and iteratively refines this model to better fit the data.

---

## Implementation Details

The script is structured into several key functions, each fulfilling a specific role in the algorithm:

- `parse_arguments()`: Parses command line arguments.
- `read_profile(file_path)`: Reads a profile matrix from a file.
- `read_sequences(file_path)`: Reads sequences from a file.
- `calculate_probabilities(...)`: Calculates probabilities for each position in each sequence.
- `update_pwm(...)`: Updates the Position Weight Matrix (PWM) based on calculated probabilities.
- `meme_algorithm(...)`: The main function that orchestrates the MEME algorithm using the above functions.
- `initialize_pwm(...)`: Initializes the PWM from a given profile.
- `initialize_positions(...)`: Initializes random positions for the motifs.

Each function is documented with Python docstrings for clarity and ease of understanding.

---

## Usage

### Prerequisites

- Python 3.10 (Managed with `pyenv`)
- `pipenv` for package management

### Installation

1. Clone the repository or download the `meme.py` script.
2. Navigate to the script's directory.

   ```bash
   cd path/to/meme.py
   ```

3. Install required packages using `pipenv`:

   ```bash
   pipenv install
   ```

### Running the Script

The script can be executed from the command line by passing three arguments:

1. Path to the file containing the profile.
2. Path to the file containing the sequences.
3. The number of iterations for the algorithm.

For example:

```bash
pipenv run python meme.py uebung_5_profile.txt uebung_5_seqs.txt 20
```

This will run the MEME algorithm with the specified profile and sequences for 20 iterations.

---

## Notes

- Ensure that the input files are formatted correctly as described in the script.
- The final PWM is printed to the console after the specified number of iterations.
