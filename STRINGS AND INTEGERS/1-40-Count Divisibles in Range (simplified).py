def count_divisible(n: int, k: int) -> int:
    sum_ = 0
    for x in range(1, n+1):
        if x % k == 0:
            sum_ += 1
    return sum_

print("Example:")
print(count_divisible(2, 1))
