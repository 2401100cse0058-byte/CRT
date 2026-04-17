def sum_of_digits(n: int) -> int:
    n = abs(n)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))