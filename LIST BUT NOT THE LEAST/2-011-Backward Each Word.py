def backward_string_by_word(text: str) -> str:
    return text if not text else " ".join(x[::-1] for x in text.split(" "))

print("Example:")
print(backward_string_by_word("olleH Hello"))
print(backward_string_by_word("Hello"))
print(backward_string_by_word("hello   world"))
