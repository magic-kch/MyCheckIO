def is_armstrong(num: int) -> bool:
    return sum(int(x) ** len(str(num)) for x in str(num)) == num

print("Example:")
print(is_armstrong(103))
