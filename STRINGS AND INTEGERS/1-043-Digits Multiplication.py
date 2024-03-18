from math import prod

def checkio(number: int) -> int:
    return prod(int(i) for i in str(number) if i != "0")

print("Example:")
print(checkio(123405))
