def except_zero(items: list[int]):
    n_items = sorted(list(filter(lambda x: x != 0, items)))
    for idx, i in enumerate(items):
        if i == 0:
            n_items.insert(idx, i)
    return n_items

print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
