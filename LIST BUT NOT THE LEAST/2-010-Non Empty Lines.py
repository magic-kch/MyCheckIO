def non_empty_lines(text: str) -> int:
    count = 0
    word = text.split("\n")
    for x in word:
        if x.strip():
            count += 1
    return count

print("Example:")
print(non_empty_lines("one\n\n simple line\n"))
