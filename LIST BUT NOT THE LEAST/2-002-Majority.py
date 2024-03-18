def is_majority(items: list[bool]) -> bool:
    return sum(items) > len(items) / 2


print("Example:")
print(is_majority([True, True, False, True, False]))
print(is_majority([True, False, False, True, False]))
print(is_majority([]))
print(is_majority([True,  False, True, False]))
