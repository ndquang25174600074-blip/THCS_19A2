
matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

row_count = 0
for r in matrix: row_count += 1
col_count = 0
for c in matrix[0]: col_count += 1

if row_count != col_count:
    print("Không phải ma trận vuông")
else:
    is_identity = True
    for i in range(row_count):
        for j in range(col_count):
            if i == j:
                if matrix[i][j] != 1: is_identity = False
            else:
                if matrix[i][j] != 0: is_identity = False
    
    if is_identity:
        print("Đây là ma trận đơn vị")
    else:
        print("Không phải ma trận đơn vị")