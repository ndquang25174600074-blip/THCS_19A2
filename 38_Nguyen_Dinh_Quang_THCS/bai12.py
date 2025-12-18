m = int(input("Nhập số hàng A: "))
n = int(input("Nhập số cột A (số hàng B): "))
p = int(input("Nhập số cột B: "))

A = []
B = []

# Nhập ma trận A
for i in range(m):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    A.append(row)

# Nhập ma trận B
for i in range(n):
    row = []
    for j in range(p):
        x = int(input())
        row.append(x)
    B.append(row)

# Nhân ma trận
C = []
for i in range(m):
    row = []
    for j in range(p):
        tong = 0
        for k in range(n):
            tong += A[i][k] * B[k][j]
        row.append(tong)
    C.append(row)

print("Ma tran ket qua:")
for i in range(m):
    print(C[i])

