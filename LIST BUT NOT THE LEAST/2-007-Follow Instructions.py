def follow(instructions: str) -> tuple[int, int] | list[int]:
    fst = 0
    snd = 0
    for x in instructions:
        if x == "f":
            snd += 1
        elif x == "b":
            snd -= 1
        elif x == "r":
            fst += 1
        elif x == "l":
            fst -= 1
    return [fst, snd]

print("Example:")
print(list(follow("fflff")))
