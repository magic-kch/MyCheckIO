def is_perfect(n: int) -> bool:
    return sum(x for x in range(1, int(n/2)+1) if n % x == 0) == n

print("Example:")
print(is_perfect(24))
