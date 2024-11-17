def edit_distance_alignment(string1, string2):
    # Making start with symbol
    str1 = "-" + string1
    str2 = "-" + string2

    # Making matrix equal to len(string1) x len(string2)
    score_mat = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    # Making same matrix
    backtrack_mat = [[None for _ in range(len(str2))] for _ in range(len(str1))]

    # First symbols of str2 (horizontal)  will be from 0 to len
    for i in range(len(str2)):
        score_mat[0][i] = i
        backtrack_mat[0][i] = "l"

    # First symbols of str1 (vertical) will be from 0 to len
    for j in range(len(str1)):
        score_mat[j][0] = j
        backtrack_mat[j][0] = "u"

    # Going through the whole matrix, by every symbol
    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            score1 = score_mat[j - 1][i - 1] + (0 if str1[j] == str2[i] else 1)  # If nuc1 == nuc2
            score2 = score_mat[j - 1][i] + 1  # If nuc1 + skip nuc2
            score3 = score_mat[j][i - 1] + 1  # If skip nuc1 + nuc2
            score_mat[j][i] = min(score1, score2, score3)
            if score_mat[j][i] == score1:
                backtrack_mat[j][i] = "d"  # No changes
            elif score_mat[j][i] == score2:
                backtrack_mat[j][i] = "u"  # In str2 there are more symbols, or it simply more rational
            elif score_mat[j][i] == score3:
                backtrack_mat[j][i] = "l"  # In str1 there are more symbols, or it simply more rational

    j = len(str1) - 1  # Because first symbol is '-'
    i = len(str2) - 1
    # Making answer strings
    aligned_1 = ""
    aligned_2 = ""
    while i != 0 or j != 0:
        direction = backtrack_mat[j][i]
        if direction == "d":  # Symbol match
            aligned_1 = str1[j] + aligned_1
            aligned_2 = str2[i] + aligned_2
            i -= 1
            j -= 1
        elif direction == "u":  # Shift in horizontal, skip in str2
            aligned_1 = str1[j] + aligned_1
            aligned_2 = "-" + aligned_2
            j -= 1
        else:  # Shift in vertical, skip in str1
            aligned_1 = "-" + aligned_1
            aligned_2 = str2[i] + aligned_2
            i -= 1

    return score_mat[len(str1) - 1][len(str2) - 1], aligned_1, aligned_2

# Reading file
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

file = open('test.txt')
lines = extract_sequence_from_input(file)
str1 = lines[0]
str2 = lines[1]

dist, s1, s2 = edit_distance_alignment(str1, str2)
print(dist, s1, s2, sep='/n')
