def extract_sequence_from_input(file):
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

f = open('test.txt')
s = extract_sequence_from_input(f)
str1 = '-' + s[0]
str2 = '-' + s[1]

score_mat = [[0 for i in range(len(str2))] for j in range(len(str1))]  # Matrix of s1 (vertical) s2 (horizontal)

for i in range(len(str2)):
    score_mat[0][i] = i  # The string corresponds to symbol -
for j in range(len(str1)):
    score_mat[j][0] = j  # The same vertical string
for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str1[j] == str2[i]:
            score1 = score_mat[j - 1][i - 1]  # Two symbols math
        else:
            score1 = score_mat[j - 1][i - 1] + 1  # No action, only mismatch
        score2 = score_mat[j - 1][i] + 1  # Deletion of nuck in str2
        score3 = score_mat[j][i - 1] + 1  # Deletion of nuck in str1
        score_mat[j][i] = min(score1, score2, score3)  # Choosing the best variant

print(score_mat[len(str1) - 1][len(str2) - 1])
