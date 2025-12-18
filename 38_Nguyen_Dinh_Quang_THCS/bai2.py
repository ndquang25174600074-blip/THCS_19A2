s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))

word = ""
for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > n:
            print(word)
        word = ""
