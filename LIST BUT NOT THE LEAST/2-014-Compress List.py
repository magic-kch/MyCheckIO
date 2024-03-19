from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    return items if len(items) < 1 else [items[0]] + [items[i] for i in range(1, len(items)) if items[i-1] != items[i]]

print(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]))
print(compress([5]))
print(compress([]))
