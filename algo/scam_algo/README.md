# Scam Detection Algorithm

This implementation uses the Aho-Corasick algorithm for efficient pattern matching to detect potential scam messages based on weighted keyword analysis.

## How It Works

### Aho-Corasick Automaton
The Aho-Corasick algorithm is a string-matching algorithm that locates elements of a finite set of strings (the "dictionary") within an input text. It matches all patterns simultaneously in a single pass through the text, making it highly efficient with O(n + m + k) complexity where:
- n = length of the text
- m = sum of the lengths of all patterns
- k = number of pattern occurrences

Key features:
- Constructs a finite state machine from the dictionary
- Uses failure links for efficient pattern matching
- Performs multiple pattern matching in linear time

### Weighted Scoring System
Each suspicious keyword in the database is assigned a weight based on its correlation with scam messages. The algorithm:
1. Identifies all matching patterns in the text
2. Calculates a cumulative score based on matched keywords and their weights
3. Determines if a message is likely to be a scam based on a threshold value

## Usage

### Prerequisites
- Python 3.8+
- C++ compiler (for the native extension)

### Building
Use the provided Makefile:
