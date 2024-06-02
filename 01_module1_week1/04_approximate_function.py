# Viết 4 functions để ước lượng các hàm số.


def factorial(x: int) -> int:

    if x < 0:
        raise ValueError("A minus number is not accepted !")
    elif x == 0 or x == 1:
        return 1

    result = 1
    for i in range(2, x + 1):
        result *= i

    return result


def approx_sin(x: float, n: int) -> float:

    result = 0
    for i in range(n):
        term = 2 * i + 1
        result += ((-1) ** i) * (x**term) / factorial(term)

    return result


def approx_cos(x: float, n: int) -> float:

    result = 0
    for i in range(n):
        term = 2 * i
        result += ((-1) ** i) * (x**term) / factorial(term)

    return result


def approx_sinh(x: float, n: int) -> float:

    result = 0
    for i in range(n):
        term = 2 * i + 1
        result += (x**term) / factorial(term)

    return result


def approx_cosh(x: float, n: int) -> float:

    result = 0
    for i in range(n):
        term = 2 * i
        result += (x**term) / factorial(term)

    return result


if __name__ == "__main__":
    x = 3.14
    n = 10
    print(f"sin({x}) ≈ {approx_sin(x, n)}")
    print(f"cos({x}) ≈ {approx_cos(x, n)}")
    print(f"sinh({x}) ≈ {approx_sinh(x, n)}")
    print(f"cosh({x}) ≈ {approx_cosh(x, n)}")
