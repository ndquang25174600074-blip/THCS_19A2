import csv

# Ghi file CSV
f = open("nhan_vien.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["ID", "Ten", "Luong"])
writer.writerow([1, "An", 60000])
writer.writerow([2, "Binh", 45000])
writer.writerow([3, "Chi", 70000])
f.close()

# Đọc file CSV
f = open("nhan_vien.csv", "r", encoding="utf-8")
reader = csv.DictReader(f)

for dong in reader:
    if int(dong["Luong"]) > 50000:
        print(dong["Ten"], "-", dong["Luong"])

f.close()
