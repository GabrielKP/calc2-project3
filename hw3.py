import math


def series36a(n):
    s_n = [1 / (k**4) for k in range(1, n + 1)]
    return sum(s_n)


def harmonic(n):
    s_n = [1 / k for k in range(1, n + 1)]
    return sum(s_n)


if __name__ == "__main__":
    print(series36a(10))
    print((1 / (3 * (11) ** 3)) + series36a(10))
    print((1 / (3 * (10) ** 3)) + series36a(10))
    print(math.pi**4 / 90)
    print(((10**5) / 3) ** (1 / 3))
    print(1 / (3 * (33**3)))

    print("E2")
    print(harmonic(100))
    print(harmonic(200))
    print(harmonic(2**13))
