def sum_upto_n(N: int) -> int:
    sum = 1

    while N > 1:
        sum = sum + N
        N = N - 1

    return sum

print("Example:")
print(sum_upto_n(10))
