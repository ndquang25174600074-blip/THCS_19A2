f1 = open("nguon.bin", "rb")
f2 = open("dich.bin", "wb")

data = f1.read(1024)
while data:
    f2.write(data)
    data = f1.read(1024)

f1.close()
f2.close()
