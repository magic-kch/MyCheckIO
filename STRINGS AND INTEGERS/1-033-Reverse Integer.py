def reverse_digits(num: int) -> int:
    return int(str(num)[::-1]) if num >= 0 else -int(str(num)[:0:-1])

print("Example:")
print(reverse_digits(-32))
