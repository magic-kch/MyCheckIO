def longest_word(sentence: str) -> str:
    return "" if sentence == "" or sentence == " " else max(sentence.split(), key=len)

print("Example:")
print(longest_word("hello world"))
