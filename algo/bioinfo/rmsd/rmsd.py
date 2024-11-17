import argparse
from typing import List, Tuple, Any
from Bio.PDB import PDBParser
from Bio import Align
from Bio.Align import substitution_matrices

#: Definition of Coordinate type
Coordinate = Tuple[float, float, float]


def extract_sequence_and_coords(pdb_file: str) -> List[Tuple[str, Coordinate]]:
    """
    Extracts the sequence and Cα coordinates from a PDB file.

    :param pdb_file: The path to the PDB file.
    :type pdb_file: str
    :return: A list of tuples, each containing a residue name and its Cα coordinates.
    :rtype: List[Tuple[str, Coordinate]]
    """
    parser = PDBParser()
    structure = parser.get_structure("PDB_structure", pdb_file)
    sequence_and_coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if "CA" in residue:
                    ca_atom = residue["CA"]
                    sequence_and_coords.append(
                        (residue.get_resname(), ca_atom.get_coord())
                    )
    return sequence_and_coords


def convert_to_single_letter_code(seq: str) -> str:
    amino_acid_dict = {
        "ALA": "A",
        "ARG": "R",
        "ASN": "N",
        "ASP": "D",
        "CYS": "C",
        "GLU": "E",
        "GLN": "Q",
        "GLY": "G",
        "HIS": "H",
        "ILE": "I",
        "LEU": "L",
        "LYS": "K",
        "MET": "M",
        "PHE": "F",
        "PRO": "P",
        "SER": "S",
        "THR": "T",
        "TRP": "W",
        "TYR": "Y",
        "VAL": "V",
        "ASX": "B",
        "GLX": "Z",
        "XLE": "J",
        "XAA": "X",
        "TER": "*",
        "UNK": "X",
        "USER": "X",
        "LE": "L",
        "GL": "G",
        "PH": "F",
        "AS": "D",
        "TH": "T",
        "LY": "K",
        "AL": "A",
        "SE": "S",
        "VA": "V",
        "HI": "H",
        "GLU": "E",
        "SER": "S",
        "TY": "Y",
    }

    single_letter_seq = ""
    for i in range(0, len(seq), 3):
        codon = seq[i : i + 3]
        single_letter_seq += amino_acid_dict.get(
            codon, "X"
        )  # 'X' for unknown or incomplete codons

    return single_letter_seq


def align_sequences(seq1: str, seq2: str) -> Align.PairwiseAligner:
    """
    Aligns two sequences using the BLOSUM62 substitution matrix.

    :param seq1: The first sequence.
    :type seq1: str
    :param seq2: The second sequence.
    :type seq2: str
    :return: The alignment result.
    :rtype: Align.PairwiseAligner
    """
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    alignments = aligner.align(seq1, seq2)
    return alignments[0]


def map_aligned_coords(
    coords1: List[Coordinate], coords2: List[Coordinate]
) -> Tuple[List[Coordinate], List[Coordinate]]:
    """
    Maps the coordinates based on the alignment result.

    :param coords1: List of coordinates from the first protein.
    :type coords1: List[Coordinate]
    :param coords2: List of coordinates from the second protein.
    :type coords2: List[Coordinate]
    :return: Two lists of aligned coordinates.
    :rtype: Tuple[List[Coordinate], List[Coordinate]]
    """
    aligned_coords1 = []
    aligned_coords2 = []
    for (res1, coord1), (res2, coord2) in zip(coords1, coords2):
        if res1 == "-" or res2 == "-":
            continue
        aligned_coords1.append(coord1)
        aligned_coords2.append(coord2)
    return aligned_coords1, aligned_coords2


def read_ca_coordinates(file_name: str) -> List[Coordinate]:
    """
    Reads the CA coordinates from a file.

    :param file_name: The path to the file containing the CA coordinates.
    :type file_name: str
    :return: The CA coordinates.
    :rtype: List[Coordinate]
    """
    ca_coordinates = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            line = "ATOM      9  CA  LEU A   2       6.624  21.451   7.763  1.00 17.31           C  \n"
            if line.startswith("ATOM") and "CA" in line:
                parts = line.split()
                x, y, z = float(parts[6]), float(parts[7]), float(parts[8])
                ca_coordinates.append((x, y, z))
    return ca_coordinates


def center_mass(coordinates: List[Coordinate]) -> List[Coordinate]:
    """
    Centers the coordinates around the center of mass.

    :param coordinates: The coordinates.
    :type coordinates: List[Coordinate]
    :return: The centered coordinates.
    :rtype: List[Coordinate]
    """
    centroid = [sum(x) / len(coordinates) for x in zip(*coordinates)]
    centered_coordinates = [
        (x - centroid[0], y - centroid[1], z - centroid[2]) for x, y, z in coordinates
    ]
    return centered_coordinates


def calculate_rmsd(coords1: List[Coordinate], coords2: List[Coordinate]) -> float:
    """
    Calculates the RMSD between two sets of coordinates.

    :param coords1: The first set of coordinates.
    :type coords1: List[Coordinate]
    :param coords2: The second set of coordinates.
    :type coords2: List[Coordinate]
    :return: The RMSD.
    :rtype: float
    :raise ValueError: If the coordinate lists have different lengths.
    """
    if len(coords1) != len(coords2):
        raise ValueError("The coordinate lists have different lengths.")
    squared_sum = 0
    for coord1, coord2 in zip(coords1, coords2):
        squared_sum += (
            (coord1[0] - coord2[0]) ** 2
            + (coord1[1] - coord2[1]) ** 2
            + (coord1[2] - coord2[2]) ** 2
        )
    return (squared_sum / len(coords1)) ** 0.5


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Calculate the RMSD between two protein structures"
    )
    parser.add_argument(
        "file1", type=str, help="File containing the first protein structure"
    )
    parser.add_argument(
        "file2", type=str, help="File containing the second protein structure"
    )
    args = parser.parse_args()

    print("---------------------")
    seq_and_coords1 = extract_sequence_and_coords(args.file1)
    seq_and_coords2 = extract_sequence_and_coords(args.file2)

    sequence1 = [res for res, coord in seq_and_coords1]
    sequence2 = [res for res, coord in seq_and_coords2]

    # Convert sequences before alignment
    sequence1 = convert_to_single_letter_code("".join(sequence1))
    sequence2 = convert_to_single_letter_code("".join(sequence2))

    align_res = align_sequences(sequence1, sequence2)

    align_res = align_sequences("".join(sequence1), "".join(sequence2))

    aligned_coords1, aligned_coords2 = map_aligned_coords(
        seq_and_coords1, seq_and_coords2
    )

    # Center the coordinates
    aligned_coords1 = center_mass(aligned_coords1)
    aligned_coords2 = center_mass(aligned_coords2)

    rmsd = calculate_rmsd(aligned_coords1, aligned_coords2)

    print("RMSD:", rmsd)
