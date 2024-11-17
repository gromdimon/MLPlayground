def consensus(strings):
    ''' Create Consensus String and Profile Matrix
    :param strings: list of DNA strings
    :return: consensus string and profile matrix
    '''
    profile_matrix = {"A": {}, "C": {}, "G": {}, "T": {}}
    for string in strings:
        for i in range(len(string)):
            if i in profile_matrix[string[i]]:
                profile_matrix[string[i]][i] += 1
            else:
                profile_matrix[string[i]][i] = 1
    consensus_string = ""
    for i in range(len(strings[0])):
        max_val = -1
        consensus_sym = ""
        for sym in profile_matrix.keys():
            if i in profile_matrix[sym]:
                if profile_matrix[sym][i] > max_val:
                    max_val = profile_matrix[sym][i]
                    consensus_sym = sym
        consensus_string += consensus_sym

    return consensus_string, profile_matrix
