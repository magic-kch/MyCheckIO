from collections.abc import Iterable


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    if border in items:
        return items[0:items.index(border)+1]
    return items

print("Example:")
print(list(remove_all_after([1, 2, 3, 4, 5], 3)))