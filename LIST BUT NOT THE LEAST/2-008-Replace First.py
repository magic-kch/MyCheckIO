from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))
    return items

# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))
