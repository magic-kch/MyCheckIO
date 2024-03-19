from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        return items[items.index(border)::]
    return items

print("Example:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
