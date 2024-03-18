def left_join(phrases: tuple[str]) -> str:
    return ",".join(phrases).replace("right", "left")

print("Example:")
print(left_join(("left", "right", "left", "stop")))
