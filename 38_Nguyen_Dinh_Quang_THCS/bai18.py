d = {'a': 1, 'b': 2, 'c': 3}
reversed_d = {}
for key in d:
    value = d[key]
    reversed_d[value] = key
print(reversed_d)