def goes_after(word: str, first: str, second: str) -> bool:
    return True if word.find(first) == word.find(second)-1 else False

print("Example:")
print(goes_after("world", "w", "o"))
