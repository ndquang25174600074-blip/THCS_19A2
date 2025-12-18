d = {'A': 70, 'B': 40, 'C': 90, 'D': 20}
filtered_d = {}
for key in d:
    if d[key] > 50:
        filtered_d[key] = d[key]
print(filtered_d)