def is_armstrong(num: int) -> bool:
    return True if (sum(int(x) ** len(str(num)) for x in str(num))) == num else False

print("Example:")
print(is_armstrong(153))
