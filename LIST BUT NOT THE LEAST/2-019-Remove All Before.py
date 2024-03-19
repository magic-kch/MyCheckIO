def remove_all_before(items: list, border: int):
    return items[items.index(border):] if border in items else items

print("Example:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
