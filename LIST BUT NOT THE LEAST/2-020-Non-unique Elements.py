def checkio(data: list[int]):
    return [i for i in data if data.count(i) > 1]

print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))
