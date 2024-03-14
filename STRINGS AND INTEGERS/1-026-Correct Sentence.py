def correct_sentence(text: str) -> str:
    if text[-1] == ".":
        return text.replace(text[0],text[0].upper(),1)
    return text.replace(text[0],text[0].upper(),1)+"."

print("Example:")
print(correct_sentence("greetings, friends"))
