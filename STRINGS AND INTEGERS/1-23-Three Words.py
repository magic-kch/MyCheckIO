def checkio(words: str) -> bool:
    s = 0
    for w in words.split():
        if w.isalpha():
            s += 1
            if s > 2: return True
        else:
            s = 0
    return False

print("Example:")
print(checkio("He is man"))
