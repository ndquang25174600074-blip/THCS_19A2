von = float(input("Nhập số tiền gửi ban đầu: "))
lai_suat = float(input("Nhập lãi suất hàng năm (%): ")) / 100
lai_1_thang = von * lai_suat * (1/12)
lai_2_quy = von * lai_suat * 0.5
lai_3_nam = von * lai_suat * 3
print("Lãi sau 1 tháng:", round(lai_1_thang, 2))
print("Lãi sau 2 quý:", round(lai_2_quy, 2))
print("Lãi sau 3 năm:", round(lai_3_nam, 2))
