A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


diff_A_B = set()
for x in A:
    if x not in B:
        diff_A_B.add(x)


diff_B_A = set()
for x in B:
    if x not in A:
        diff_B_A.add(x)


intersection = set()
for x in A:
    if x in B:
        intersection.add(x)


union = set()
for x in A: union.add(x)
for x in B: union.add(x)

print("A - B:", diff_A_B)
print("B - A:", diff_B_A)
print("Giao:", intersection)
print("Hợp:", union)