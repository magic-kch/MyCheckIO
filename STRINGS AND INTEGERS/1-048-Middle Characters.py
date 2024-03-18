def middle(text: str) -> str:
    if len(text) % 2 == 0:
        return text[int(len(text)/2)-1:int(len(text)/2) +1]
    return text[int(len(text)/2):int(len(text)/2)+1]

print("Example:")
print(middle("example"))
