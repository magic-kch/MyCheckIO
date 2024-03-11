def longest_word(sentence: str) -> str:
    if sentence == "" or sentence == " ":
        return ""
    max_ = 0
    for word in sentence.split():
        if len(word) > max_:
            max_ = len(word)
            st = word
    return st

print("Example:")
print(longest_word("hello world"))
