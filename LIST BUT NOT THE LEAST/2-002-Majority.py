def is_majority(items: list[bool]) -> bool:
    if len(items) < 1:
        return False
    elif items.count(False) >= items.count(True):
        return False
    return True

print("Example:")
print(is_majority([True, True, False, True, False]))
