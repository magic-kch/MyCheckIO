def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))

print("Example:")
print(end_zeros(0))
