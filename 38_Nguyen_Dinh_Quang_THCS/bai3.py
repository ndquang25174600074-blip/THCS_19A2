s = input("Nhập chuỗi: ")

result = ""
prev_space = True

for ch in s:
    if ch != " ":
        result += ch
        prev_space = False
    else:
        if not prev_space:
            result += " "
            prev_space = True

print(result)
