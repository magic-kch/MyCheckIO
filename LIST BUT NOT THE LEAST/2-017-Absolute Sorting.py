def checkio(values: list) -> list:
    return sorted(values, key=lambda n: abs(n))

print("Example:")
print(checkio([-20, -5, 10, 15]))
