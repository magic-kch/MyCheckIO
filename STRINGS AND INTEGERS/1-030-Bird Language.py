def translation(text: str) -> str:
    res = []
    for word in text.split():
        tmp = ""
        x = 0

        while x < len(word):
            if word[x] not in "aeiouy":
                tmp += word[x]
                x += 2

            else:
                tmp += word[x]
                x += 3

        res.append(tmp)

    return " ".join(res)


print("Example:")
print(translation("hieeelalaooo"))