def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Example:")
print(factorial(4))
