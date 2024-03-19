def backward_string_by_word(text: str) -> str:
    if not text:
        return text
    ntext = []
    for x in text.split(" "):
        ntext.append(x[::-1])
    return " ".join(ntext)

print("Example:")
print(backward_string_by_word("olleH Hello"))
print(backward_string_by_word("Hello"))
print(backward_string_by_word("hello   world"))
