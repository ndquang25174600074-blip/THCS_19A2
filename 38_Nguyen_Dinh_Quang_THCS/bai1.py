s = input("Nhập chuỗi: ")

chu_cai = 0
chu_so = 0
ky_tu_dac_biet = 0

for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        chu_cai += 1
    elif '0' <= ch <= '9':
        chu_so += 1
    else:
        ky_tu_dac_biet += 1

print("Số chữ cái:", chu_cai)
print("Số chữ số:", chu_so)
print("Số ký tự đặc biệt:", ky_tu_dac_biet)
