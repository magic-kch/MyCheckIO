from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) <= 1:
        return items
    else:
        st = items.pop(0)
        items.append(st)
    return items

# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))
