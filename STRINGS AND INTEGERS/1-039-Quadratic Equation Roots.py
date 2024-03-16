def quadratic_roots(a: int, b: int, c: int)
    D = b ** 2 - 4 * a * c
    if D < 0:
        return ["No real roots"]
    elif D == 0:
        return [-b / (2 * a), -b / (2 * a)]
    elif D > 0:
        D = D ** 0.5
    return [(-b + D) / (2 * a), (-b - D) / (2 * a)]

print(quadratic_roots(1, -3, 2))
print(quadratic_roots(1,2,3))
print(quadratic_roots(1, 2, 1))