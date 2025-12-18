n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

k = int(input())
k = k % n

b = []

for i in range(n - k, n):
    b.append(a[i])
for i in range(n - k):
    b.append(a[i])

print(b)
