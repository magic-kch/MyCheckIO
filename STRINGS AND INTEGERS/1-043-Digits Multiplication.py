def checkio(number: int) -> int:
    res = 1
    for i in str(number):
        if i != "0":
            res *= int(i)
    return res

print("Example:")
print(checkio(123405))
