tong_keo = int(input("Nhập tổng số kẹo: "))
so_hs = int(input("Nhập số học sinh: "))

moi_em = tong_keo // so_hs
thua = tong_keo % so_hs

print("Mỗi học sinh nhận:", moi_em, "kẹo")
print("Số kẹo còn thừa:", thua)
