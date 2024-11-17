def minkowski_difference(str1, str2):
    # Counting difference for every pair of values
    differences = []
    for s1 in str1:
        for s2 in str2:
            differences.append(round(s1 - s2, 5))

    # Making cortage with times of value appears in difference list
    minkowski_cort = {}
    for value in differences:
        minkowski_cort[value] = differences.count(value)

    # Choosing the max value and max index to return them
    max_value = -1
    max_index = 0
    for index, value in minkowski_cort.items():
        if minkowski_cort[index] > max_value:
            max_index = index
            max_value = minkowski_cort[index]

    return max_value, max_index

# Reading file
file = open('test.txt')
lines = file.read().splitlines()
string1 = [float(x) for x in lines[0].split()]
string2 = [float(x) for x in lines[1].split()]

ans = minkowski_difference(string1, string2)
print(ans[0], ans[1])
