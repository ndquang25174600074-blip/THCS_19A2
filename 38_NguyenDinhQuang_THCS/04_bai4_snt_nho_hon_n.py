# Bài 4: Tìm tất cả các số nguyên tố nhỏ hơn n (sieve of Eratosthenes)
def primes_less_than(n):
    if n <= 2:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    p = 2
    while p * p < n:
        if sieve[p]:
            for multiple in range(p*p, n, p):
                sieve[multiple] = False
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def main():
    try:
        n = int(input("Nhập n (tìm các số nguyên tố < n): ").strip())
    except ValueError:
        print("Vui lòng nhập số nguyên dương.")
        return
    primes = primes_less_than(n)
    print(f"Các số nguyên tố nhỏ hơn {n}:")
    if primes:
        print(', '.join(map(str, primes)))
    else:
        print("(Không có)")

if __name__ == '__main__':
    main()
