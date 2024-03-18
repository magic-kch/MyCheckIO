def is_majority(items: list[bool]) -> bool:
    return False if len(items) < 1 else not (items.count(False) >= items.count(True))


print("Example:")
print(is_majority([True, True, False, True, False]))
print(is_majority([True, False, False, True, False]))
print(is_majority([]))
print(is_majority([True,  False, True, False]))
