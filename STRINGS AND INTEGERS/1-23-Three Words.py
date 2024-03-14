def checkio(words: str) -> bool:
<<<<<<< HEAD
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
=======
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
>>>>>>> parent of 4f9b27f (add 1-23-Three Words_mod)
