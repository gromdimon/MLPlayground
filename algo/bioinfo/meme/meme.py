import argparse
import numpy as np
from typing import List


def parse_arguments() -> argparse.Namespace:
    """
    Parses the command line arguments.

    :return: The parsed arguments.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="MEME Algorithm Implementation")
    parser.add_argument("profile_file", type=str, help="File containing the profile")
    parser.add_argument("sequence_file", type=str, help="File containing the sequences")
    parser.add_argument("iterations", type=int, help="Number of iterations")

    args = parser.parse_args()
    return args


def read_profile(file_path: str) -> List[List[float]]:
    """
    Reads the profile from a file.

    :param file_path: The path to the file containing the profile.
    :type file_path: str
    :return: The profile.
    :rtype: List[List[float]]
    """
    profile = []
    with open(file_path, "r") as file:
        for line in file:
            row = [float(num) for num in line.split()]
            profile.append(row)
    return profile


def read_sequences(file_path: str) -> List[str]:
    """
    Reads the sequences from a file.

    :param file_path: The path to the file containing the sequences.
    :type file_path: str
    :return: The sequences.
    :rtype: List[str]
    """
    sequences = []
    with open(file_path, "r") as file:
        for line in file:
            sequences.append(line.strip())  # Remove newline characters
    return sequences


def calculate_probabilities(
    sequences: List[str], pwm: np.ndarray, motif_width: int
) -> List[List[float]]:
    """
    Calculates the probabilities for each sequence and each position in the sequence.

    :param sequences: The sequences.
    :type sequences: List[str]
    :param pwm: The PWM.
    :type pwm: np.ndarray
    :param motif_width: The width of the motif.
    :type motif_width: int
    :return: The probabilities.
    :rtype: List[List[float]]
    """
    probabilities = []
    for seq in sequences:
        prob = []
        for i in range(len(seq) - motif_width + 1):
            subseq = seq[i : i + motif_width]
            p = 1
            for j, char in enumerate(subseq):
                if char == "A":
                    p *= pwm[0][j]
                elif char == "C":
                    p *= pwm[1][j]
                elif char == "G":
                    p *= pwm[2][j]
                elif char == "T":
                    p *= pwm[3][j]
            prob.append(p)
        probabilities.append(prob)
    return probabilities


def update_pwm(
    sequences: List[str], probabilities: List[List[float]], motif_width: int
) -> np.ndarray:
    """
    Updates the PWM.

    :param sequences: The sequences.
    :type sequences: List[str]
    :param probabilities: The probabilities.
    :type probabilities: List[List[float]]
    :param motif_width: The width of the motif.
    :type motif_width: int
    :return: The updated PWM.
    :rtype: np.ndarray
    """
    pwm = np.zeros((4, motif_width))
    for j in range(motif_width):
        for i, seq in enumerate(sequences):
            subseq = seq[i : i + motif_width]
            total_prob = sum(probabilities[i])
            for k, char in enumerate(subseq):
                if char == "A":
                    pwm[0][k] += probabilities[i][j] / total_prob
                elif char == "C":
                    pwm[1][k] += probabilities[i][j] / total_prob
                elif char == "G":
                    pwm[2][k] += probabilities[i][j] / total_prob
                elif char == "T":
                    pwm[3][k] += probabilities[i][j] / total_prob
    return pwm / pwm.sum(axis=0)


def meme_algorithm(
    sequences: List[str], profile: List[List[float]], motif_width: int, iterations: int
) -> np.ndarray:
    """
    Runs the MEME algorithm.

    :param sequences: The sequences.
    :type sequences: List[str]
    :param profile: The profile.
    :type profile: List[List[float]]
    :param motif_width: The width of the motif.
    :type motif_width: int
    :param iterations: The number of iterations.
    :type iterations: int
    :return: The final PWM.
    :rtype: np.ndarray
    """
    pwm = initialize_pwm(profile)
    for _ in range(iterations):
        probabilities = calculate_probabilities(sequences, pwm, motif_width)
        pwm = update_pwm(sequences, probabilities, motif_width)
    return pwm


def initialize_pwm(profile: List[List[float]]) -> np.ndarray:
    """
    Initializes the PWM.

    :param profile: The profile.
    :type profile: List[List[float]]
    :return: The PWM.
    :rtype: np.ndarray
    """
    pwm = np.array(profile)
    return pwm


def initialize_positions(sequences: List[str], motif_width: int) -> List[int]:
    """
    Initializes the positions of the motifs.

    :param sequences: The sequences.
    :type sequences: List[str]
    :param motif_width: The width of the motif.
    :type motif_width: int
    :return: The positions.
    :rtype: List[int]
    """
    return [np.random.randint(0, len(seq) - motif_width + 1) for seq in sequences]


def main() -> None:
    """
    Main function.

    We implement the MEME algorithm as described in the lecture slides.

    The script takes three arguments:
    - The path to the file containing the profile
    - The path to the file containing the sequences
    - The number of iterations

    All arguments are read and MEME algorithm is run.
    After the algorithm has finished, the final PWM is printed.
    """
    args = parse_arguments()

    profile_file = args.profile_file
    sequence_file = args.sequence_file
    iterations = args.iterations

    profile = read_profile(profile_file)
    sequences = read_sequences(sequence_file)
    motif_width = len(
        profile[0]
    )  # Assuming motif width is the length of a row in the profile

    final_pwm = meme_algorithm(sequences, profile, motif_width, iterations)
    print(f"Final PWM: \n{final_pwm}")


if __name__ == "__main__":
    main()
