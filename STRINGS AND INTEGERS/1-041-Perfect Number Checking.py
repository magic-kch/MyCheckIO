def is_perfect(n: int) -> bool:
    sum = 0
    for x in range(1,int(n/2)+1):
        if n % x == 0:
            sum += x
    if sum == n:
        return True
    return False

print("Example:")
print(is_perfect(28))
