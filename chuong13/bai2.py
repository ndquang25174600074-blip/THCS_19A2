f = open("vanban.txt", "r", encoding="utf-8")
noi_dung = f.read()
f.close()

tu_dien = {}

for tu in noi_dung.split():
    if tu in tu_dien:
        tu_dien[tu] += 1
    else:
        tu_dien[tu] = 1

for tu in tu_dien:
    print(tu, ":", tu_dien[tu])
