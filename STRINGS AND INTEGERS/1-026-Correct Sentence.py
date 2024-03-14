def correct_sentence(text: str) -> str:
    return text.replace(text[0],text[0].upper(),1) if text[-1] == "." else  text.replace(text[0],text[0].upper(),1)+"."

print("Example:")
print(correct_sentence("greetings, friends"))
