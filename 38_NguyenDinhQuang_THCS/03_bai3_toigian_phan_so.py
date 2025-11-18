# Bài 3: Tối giản phân số
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def reduce_fraction(num, den):
    if den == 0:
        raise ZeroDivisionError("Mẫu số không được bằng 0.")
    sign = -1 if (num * den) < 0 else 1
    num, den = abs(num), abs(den)
    g = gcd(num, den)
    num //= g
    den //= g
    return (sign * num, den)

def main():
    try:
        num = int(input("Nhập tử số: ").strip())
        den = int(input("Nhập mẫu số: ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên.")
        return
    try:
        a, b = reduce_fraction(num, den)
    except ZeroDivisionError as e:
        print(e)
        return
    print(f"Phân số tối giản: {a}/{b}")

if __name__ == '__main__':
    main()
