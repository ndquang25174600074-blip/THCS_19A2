a = input("Nhập các số, cách nhau bằng dấu cách: ")

tong_chan = 0
tong_le = 0
so = ""

for ch in a:
    if ch != " ":
        so += ch
    else:
        x = int(so)
        if x % 2 == 0:
            tong_chan += x
        else:
            tong_le += x
        so = ""

# xử lý số cuối cùng
x = int(so)
if x % 2 == 0:
    tong_chan += x
else:
    tong_le += x

print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)

