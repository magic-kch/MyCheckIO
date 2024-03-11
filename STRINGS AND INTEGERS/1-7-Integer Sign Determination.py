def determine_sign(num: int) -> str:
    if num > 0:
        return "positive"
    elif num == 0:
        return "zero"
    return "negative"

print("Example:")
print(determine_sign(11))
