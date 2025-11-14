can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

BMI = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI là:", round(BMI, 2))
