m = int(input("Nhập số hàng: "))

a = []

for i in range(m):
    s = input()
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

max_sum = None
index = 0

for i in range(m):
    tong = 0
    for x in a[i]:
        tong += x

    if max_sum is None or tong > max_sum:
        max_sum = tong
        index = i

print(index)
