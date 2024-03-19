def is_ascending(items: list[int]) -> bool:
    for i in range(len(items)-1):
        if items[i] >= items[i+1]:
            return False
    return True

print("Example:")
print(is_ascending([-5, 10, 99, 123456]))
