def left_join(phrases: tuple[str]) -> str:
    lst = []
    for word in phrases:
        if "right" in word:
            lst.append(word.replace("right", "left"))
        else:
            lst.append(word)
    return ",".join(lst)

print("Example:")
print(left_join(("left", "right", "left", "stop")))
