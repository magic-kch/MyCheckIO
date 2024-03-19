def is_ascending(items: list[int]) -> bool:
    return sorted(set(items)) == items

print("Example:")
print(is_ascending([-5, 10, 1, 99, 123456]))
