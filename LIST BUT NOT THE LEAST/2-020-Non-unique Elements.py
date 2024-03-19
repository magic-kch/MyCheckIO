from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    new_data = []
    for i in data:
        if data.count(i) > 1:
            new_data.append(i)
    return new_data

print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))
