# Bài 1: Kiểm tra số chính phương
import math

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(math.isqrt(n))
    return r*r == n

def main():
    try:
        s = input("Nhập một số nguyên (enter để thoát): ").strip()
        if not s:
            return
        n = int(s)
    except ValueError:
        print("Vui lòng nhập số nguyên.")
        return
    if is_perfect_square(n):
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")

if __name__ == '__main__':
    main()
