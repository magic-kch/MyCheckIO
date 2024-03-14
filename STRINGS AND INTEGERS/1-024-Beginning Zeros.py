def beginning_zeros(a: str) -> int:
    sum_ = 0
    for x in a:
        if x == "0":
            sum_ += 1
        else:
            break
    return sum_

print("Example:")
print(beginning_zeros("00000000000000010"))
