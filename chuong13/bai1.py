f = open("vanban.txt", "r", encoding="utf-8")
noi_dung = f.read()
f.close()

so_tu = len(noi_dung.split())
print("Tong so tu:", so_tu)
