id_can_sua = input("Nhap ID: ")
gia_moi = input("Nhap gia moi: ")

f = open("san_pham.txt", "r")
dong = f.readlines()
f.close()

ds_moi = []

for d in dong:
    if d.startswith(id_can_sua + ","):
        phan = d.strip().split(",")
        phan[2] = gia_moi
        ds_moi.append(",".join(phan) + "\n")
    else:
        ds_moi.append(d)

f = open("san_pham.txt", "w")
f.writelines(ds_moi)
f.close()
