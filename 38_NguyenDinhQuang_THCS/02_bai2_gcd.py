# Bài 2: Tìm ước chung lớn nhất (GCD) của hai số
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        a = int(input("Nhập số thứ nhất: ").strip())
        b = int(input("Nhập số thứ hai: ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên.")
        return
    print(f"Ước chung lớn nhất của {a} và {b} là {gcd(a,b)}")

if __name__ == '__main__':
    main()
