n = int(input("Nhập n: "))

a = []

for i in range(n):
    s = input("Nhập hàng " + str(i + 1) + ": ")
    row = []
    so = ""

    for ch in s:
        if ch != " ":
            so += ch
        else:
            row.append(int(so))
            so = ""
    row.append(int(so))

    a.append(row)

tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]

print("Tổng đường chéo phụ:", tong)
