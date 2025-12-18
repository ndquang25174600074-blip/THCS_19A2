
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

is_symmetric = True
n = 0
for row in matrix:
    n += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

if is_symmetric:
    print("Đây là ma trận đối xứng")
else:
    print("Đây không phải là ma trận đối xứng")