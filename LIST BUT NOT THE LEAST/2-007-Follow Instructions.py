def follow(ins: str) -> tuple[int, int] | list[int]:
    return [ins.count("r") - ins.count("l"), ins.count("f") - ins.count("b")]

print("Example:")
print(list(follow("fflff")))
