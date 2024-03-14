def checkio(words: str) -> bool:
    for w in words.split():
        if not w.isalpha():
            return False
    return True

print("Example:")
print(checkio("Hello World 1 hello"))
