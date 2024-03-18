def middle(text: str) -> str:
    a = int(len(text)/2)
    return text[a-1:a+1] if len(text) % 2 == 0 else text[a:a+1]

print("Example:")
print(middle("example"))
print(middle("examples"))
