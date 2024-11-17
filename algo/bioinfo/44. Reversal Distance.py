# This code i found primarly in medium from Matt West

def extract_sequence_from_input(file):
    '''
    Reading fasta format
    :param fp: multiples string on different lines
    :return: sequences as list
    '''
    sequences = []
    result = ""
    for line in file:
        if ">" in line:
            sequences.append(result)  # Appending sequence list with final seq
            result = ""  # Initiation of a new seq
        else:
            if "\n" in line:
                result += line[:len(line) - 1]  # Lengthening of sequence
            else:
                result += line
    sequences.append(result)  # Appending list with last seq
    sequences.remove('')
    return sequences

def make_reverse(sequence, start_index, end_index):
    prefix = sequence[:start_index]
    reversed_subsequence = sequence[start_index:end_index][::-1]
    suffix = sequence[end_index:]
    return prefix + reversed_subsequence + suffix


def find_breakpoints(sequence, target_sequence):
    breakpoints = []
    for index in range(len(sequence) - 1):
        current_element = sequence[index]
        adjacent_element = sequence[index + 1]
        if abs(target_sequence.index(current_element) - target_sequence.index(adjacent_element)) != 1:
            # If two symbols do not follow each other
            breakpoints.append(index + 1)
    return breakpoints


def find_min_reverse(sequences, target_sequence):
    # Take sequences from previous step and perform function
    reversals = []
    for sequence in sequences:
        breakpoints = find_breakpoints(sequence, target_sequence)
        for start_index_i in range(len(breakpoints) - 1):  # All possible reversals for the step
            for end_index_i in range(start_index_i + 1, len(breakpoints)):
                reversals.append(make_reverse(sequence, breakpoints[start_index_i], breakpoints[end_index_i]))
    min_bp = len(target_sequence)
    minimum_reversals = []
    for reversal in reversals:  # Choosing reversals with minimum breakpoints
        num_breakpoints = len(find_breakpoints(reversal, target_sequence))
        if num_breakpoints < min_bp:
            min_bp = num_breakpoints
            minimum_reversals = [reversal]
        elif num_breakpoints == min_bp:
            minimum_reversals.append(reversal)
    return minimum_reversals


def reversal_distance(sequence, target_sequence):
    sequence = ["-"] + sequence + ["+"]
    target_sequence = ["-"] + target_sequence + ["+"]
    reversals = 0
    current_sequences = [sequence]
    while target_sequence not in current_sequences:
        current_sequences = find_min_reverse(current_sequences, target_sequence)  # Go throw each step, adding to reversal_counter
                                                                                  # and choosing sequence with minimum breakpoints for next step
        reversals += 1
    return reversals


if __name__ == "__main__":
    with open('test.txt') as file:
        lines = file.readlines()
        input_lines = [line.rstrip() for line in lines]
    all_dist = []
    for idx in range(0, len(input_lines), 3):
        P1 = list(map(int, input_lines[idx].split()))
        P2 = list(map(int, input_lines[idx + 1].split()))

        dist = reversal_distance(P1, P2)
        all_dist.append(dist)

    print(' '.join(map(str, all_dist)))
