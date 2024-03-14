def goes_after(word: str, first: str, second: str) -> bool:
    if word.find(first) == word.find(second)-1:
        return True
    return False

print("Example:")
print(goes_after("world", "w", "o"))
