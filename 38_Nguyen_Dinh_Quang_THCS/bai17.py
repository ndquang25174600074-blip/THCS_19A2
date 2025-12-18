d = {'a': 10, 'b': 50, 'c': 30}
max_val = None
max_key = None

for key in d:
    if max_val is None or d[key] > max_val:
        max_val = d[key]
        max_key = key
print("Key có giá trị lớn nhất:", max_key)