from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    if len(items) < 1:
        return items
    new = [items[0],]
    for i in range(1, len(items)):
        if new[-1] != items[i]:
            new.append(items[i])
    return new

print(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]))
print(compress([5]))
print(compress([]))
