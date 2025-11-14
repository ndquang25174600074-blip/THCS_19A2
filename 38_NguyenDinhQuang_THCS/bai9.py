so_kwh = int(input("Nhập số kWh tiêu thụ: "))
if so_kwh <= 100:
    tien = so_kwh * 1678
elif so_kwh <= 200:
    tien = 100 * 1678 + (so_kwh - 100) * 1734
else:
    tien = 100 * 1678 + 100 * 1734 + (so_kwh - 200) * 2014
print("Tổng tiền điện phải trả là:", tien, "VNĐ")
