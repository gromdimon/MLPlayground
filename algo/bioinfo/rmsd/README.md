# RMSD (Root Mean Square Deviation) Calculator

This tool calculates the Root Mean Square Deviation (RMSD) between two protein structures using their Cα atom coordinates. RMSD is a standard measure used in structural biology to quantify the structural similarity between proteins.

## How It Works

The algorithm performs the following steps:
1. Extracts Cα coordinates and sequences from PDB files
2. Aligns sequences using BLOSUM62 matrix
3. Centers structures around their center of mass
4. Calculates RMSD between aligned coordinates

### Key Features
- Supports PDB file format
- Uses BioPython for PDB parsing and sequence alignment
- Implements sequence alignment using BLOSUM62 substitution matrix
- Centers structures before RMSD calculation
- Handles missing residues and alignment gaps

## Data

The data is in `pdb1.txt` and `pdb2.txt` files. This are examples of protein structures in PDB format.

## Usage

```bash
python3 ./rmsd.py pdb1.txt pdb2.txt
