def between_markers(text: str, start: str, end: str) -> str:
    return text[text.find(start)+1:text.find(end)]

print("Example:")
print(between_markers("What is >apple<", ">", "<"))
