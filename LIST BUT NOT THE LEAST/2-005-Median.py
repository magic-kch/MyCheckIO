def checkio(data: list[int]) -> int | float:
    data.sort()
    n = len(data) // 2
    return sum(data[n-1:n+1]) / 2 if len(data) % 2 == 0 else data[n]

print("Example:")

# These "asserts" are used for self-checking
print(checkio([1, 2, 3, 4, 5]), " == 3")
print(checkio([3, 1, 2, 5, 3]), " == 3")
print(checkio([1, 300, 2, 200, 1]), " == 2")
print(checkio([3, 6, 20, 99, 10, 15]), " == 12.5")
