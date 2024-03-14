def beginning_zeros(a: str) -> int:
    sum_ = 0
    if a[0] == "0":
        for x in a:
            if x != "0":
                break
            sum_ += 1
    return sum_

print("Example:")
print(beginning_zeros("0010"))
