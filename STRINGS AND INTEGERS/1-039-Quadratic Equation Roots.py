def quadratic_roots(a: int, b: int, c: int):
    det = b ** 2 - 4 * a * c
    return ["No real roots"] if det < 0 else [(-b + det ** 0.5) / (2 * a), (-b - det ** 0.5) / (2 * a)]

print(quadratic_roots(1, -3, 2))
print(quadratic_roots(1,2,3))
print(quadratic_roots(1, 2, 1))
