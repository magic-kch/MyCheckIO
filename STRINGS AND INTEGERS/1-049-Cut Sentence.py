def cut_sentence(line: str, length: int) -> str:
    if len(line) <= length:
        return line
    elif length == 1 or line.index(" ") > length:
        return "..."
    else:
        return line[:line.rfind(" ", 0, length + 1)] + "..."

print("Example:")
print(cut_sentence("Hi my name is Alex", 4))
