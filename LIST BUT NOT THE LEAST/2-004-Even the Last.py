def checkio(array: list[int]) -> int:
    return 0 if len(array) == 0 else sum(array[0::2]) * array[-1]

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
