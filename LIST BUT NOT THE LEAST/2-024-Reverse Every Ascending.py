from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    if len(items) <= 1:
        return items
    if items == sorted(set(items)):
        return items[::-1]
    res = []
    tmp = [items[0]]
    for i in range(1, len(items)):
        if items[i - 1] < items[i]:
            tmp.append(items[i])
        else:
            res.extend(tmp[::-1])
            tmp = [items[i]]
    res.extend(tmp[::-1])
    return res



print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))
print(list(reverse_ascending([1, 1, 2])))
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))
