luong_cb = float(input("Nhập lương cơ bản: "))
ngay_cong = int(input("Nhập số ngày công: "))
luong_ngay = luong_cb / 22
luong_thuc = luong_ngay * ngay_cong
if ngay_cong > 22:
    luong_thuc += luong_thuc * 0.1
elif ngay_cong < 22:
    luong_thuc -= luong_thuc * 0.05
    
print("Tổng lương thực nhận:", round(luong_thuc, 2))
