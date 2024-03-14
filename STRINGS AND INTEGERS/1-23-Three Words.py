def checkio(words: str) -> bool:
    lst = words.split()
    ok = 0
    for word in lst:
        try:
            if int(word):
                ok = 0
        except ValueError:
            ok += 1
            if ok > 2:
                return True

    return False

print("Example:")
print(checkio("Hello World hello"))
