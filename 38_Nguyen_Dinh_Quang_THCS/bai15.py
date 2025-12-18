tup = (1, 2, 3, 4, 5, 6)
chan = []
le = []
tong_chan = 0
tong_le = 0

for x in tup:
    if x % 2 == 0:
        chan += [x]
        tong_chan += x
    else:
        le += [x]
        tong_le += x

tuple_chan = tuple(chan)
tuple_le = tuple(le)

print(f"Chẵn: {tuple_chan}, Tổng: {tong_chan}")
print(f"Lẻ: {tuple_le}, Tổng: {tong_le}")