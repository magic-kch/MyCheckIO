def remove_all_after(items: list[int], border: int):
    return items[:items.index(border)+1] if border in items else items

print("Example:")
print(list(remove_all_after([1, 2, 3, 4, 5], 3)))