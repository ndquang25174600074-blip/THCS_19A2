n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    a.append(int(input()))
max1 = a[0]
max2 = None
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and (max2 is None or x > max2):
        max2 = x
print("Số lớn thứ hai:", max2)
