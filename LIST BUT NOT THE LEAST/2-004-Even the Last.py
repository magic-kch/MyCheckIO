def checkio(array: list[int]) -> int:
    sum = 0
    if len(array) == 0:
        return 0
    for i in range(0,len(array),2):
        sum += array[i]
    return sum * array[-1]

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
