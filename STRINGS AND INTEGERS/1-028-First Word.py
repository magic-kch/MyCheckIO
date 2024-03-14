def first_word(text: str) -> str:
    res = ''
    for char in text:
        if char.isalpha() or char == "'":
            res += char
        elif not char.isalpha() and len(res) > 0:
            return res
    return res

print("Example:")
print(first_word("Hello world"))
