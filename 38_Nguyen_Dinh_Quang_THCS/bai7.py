s = input("Nhập danh sách số: ")
k = int(input("Nhập k: "))

a = []
so = ""


for ch in s:
    if ch != " ":
        so += ch
    else:
        a.append(int(so))
        so = ""
a.append(int(so))

n = len(a)
co_cap = False

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            print(a[i], a[j])
            co_cap = True

if not co_cap:
    print("Không có cặp nào thỏa mãn")
