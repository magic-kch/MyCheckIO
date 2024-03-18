def checkio(text: str) -> str:
    text = text.lower()
    text_set = set(text)
    res = {}
    restr = ""
    for i in text_set:
        if i.isalpha():
            res[i] = (text.count(i))
    for k, v in res.items():
        if v == max(res.values()):
            restr += k
    if len(restr) > 1:
        return min(restr)
    return max(restr)

print("Example:")
print(checkio("Hello World!"))
print(checkio("one"))
