def checkio(data: list[int]) -> int | float:
    res = sorted(data)
    if len(data) % 2 != 0:
        return res[int(len(res) / 2)]

    return float((res[int(len(res) / 2) - 1] + res[int(len(res) / 2)])) / 2

print("Example:")

# These "asserts" are used for self-checking
print(checkio([1, 2, 3, 4, 5]), " == 3")
print(checkio([3, 1, 2, 5, 3]), " == 3")
print(checkio([1, 300, 2, 200, 1]), " == 2")
print(checkio([3, 6, 20, 99, 10, 15]), " == 12.5")
