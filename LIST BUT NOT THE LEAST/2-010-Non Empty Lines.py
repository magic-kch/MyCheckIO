def non_empty_lines(text: str) -> int:
    word = text.split("\n")
    return sum(1 for x in word if x.strip())

print("Example:")
print(non_empty_lines("\none\n\n simple\n line\n"))
