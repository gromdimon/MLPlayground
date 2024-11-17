def longest_common_subsequence(v, w):
    current = [''] * (len(v) + 1)
    for nuckl_w in w:
        last, current = current, ['']  # Saving previous result
        for index_v, nuckl_v in enumerate(v):
            current.append(last[index_v] + nuckl_w if nuckl_w == nuckl_v else max(last[index_v + 1], current[-1], key=len))
            # Adding letter to subseq or choosing the previous subseq
    return (current[-1])

def shortest_common_supersequence(v, w):
    lcsq_string = longest_common_subsequence(v, w)

    scs_string = ""
    i = 0
    j = 0
    for char in lcsq_string:
        if i < len(v):  # Adding symbols from v_string
            while v[i] != char:
                scs_string += v[i]
                i += 1
            i += 1
        if j < len(w):  # Adding symbols from w_string
            while w[j] != char:
                scs_string += w[j]
                j += 1
            j += 1
        scs_string += char

    #  Adding final symbols
    if i < len(v):
        scs_string += v[i:]
    if j < len(w):
        scs_string += w[j:]

    return scs_string

v, w = input(), input()
print(shortest_common_supersequence(v, w))
