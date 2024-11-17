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

def find_reverse_index(sequence, start_index, end_index):
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
        breakpoints = find_breakpoints(sequence[0], target_sequence)
        for start_index_i in range(len(breakpoints) - 1):
            for end_index_i in range(start_index_i + 1, len(breakpoints)):
                reversals.append((make_reverse(sequence[0], breakpoints[start_index_i], breakpoints[end_index_i]),
                                  sequence[1] + [(breakpoints[start_index_i] - 1, breakpoints[end_index_i] - 1)]))
    min_bp = len(target_sequence)
    minimum_reversals = []
    for reversal in reversals:  # Choosing reversals with minimum breakpoints
        num_breakpoints = len(find_breakpoints(reversal[0], target_sequence))
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
    current_sequences = [(sequence, [])]
    while target_sequence not in [current_sequence[0] for current_sequence in current_sequences]:
        current_sequences = find_min_reverse(current_sequences, target_sequence)   # Go throw each step, adding to reversal_counter
                                                                                   # and choosing sequence with minimum breakpoints for next step
        reversals += 1
    return reversals, current_sequences


def build_index_history(reversal_history):
    index_history = []
    for reversal_start, reversal_end in reversal_history:
        index_history.append([reversal_start + 1, reversal_end])
    return index_history


if __name__ == "__main__":

    with open('test.txt') as file:
        lines = file.readlines()
        input_lines = [line.rstrip() for line in lines]
    sequence = list([x for x in input_lines[0].split()])
    target_sequence = list([x for x in input_lines[1].split()])

    rev_distance, histories = reversal_distance(sequence, target_sequence)
    indexes_history = build_index_history(histories[0][1])
    print(rev_distance)
    for i in indexes_history:
        print(*i)
