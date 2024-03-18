def is_all_upper(text: str) -> bool:
    for char in text:
        if char.islower():
            return False
    return True

print("Example:")
print(is_all_upper("ALL UPPER"))
