from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    if items.count(0) < 1:
        return sorted(items)
    elif items.count(0) == len(items):
        return items
    n_items = sorted(items)
    n_items = n_items[items.count(0):]
    for idx, i in enumerate(items):
        if i == 0:
            n_items.insert(idx, 0)
    return n_items

print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
