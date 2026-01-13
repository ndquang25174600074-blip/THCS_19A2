ds = [1, 2, 3, 4, 5]
f = open("so_nguyen.txt", "w")
for so in ds:
    f.write(str(so) + "\n")
f.close()
