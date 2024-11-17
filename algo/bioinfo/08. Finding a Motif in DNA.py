def find_motif(string, motif):
    # Finding similar to the motif of the segments in the string
    spis = []
    for i in range(len(string)):
        if string[i:i + len(motif)] == motif:   # Condition, that motif equal string from i to k
            spis.append(i + 1)

# Reading files
string, motive = input(), input()

