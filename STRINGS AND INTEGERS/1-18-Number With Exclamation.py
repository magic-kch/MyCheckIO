def factorial(n: int) -> int:
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)

print("Example:")
print(factorial(4))
