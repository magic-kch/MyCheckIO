def is_armstrong(num: int) -> bool:
    sum = 0
    for x in str(num):
        a = int(x)
        if a == 0:
            continue
        sum += (a ** len(str(num)))

    if num == sum:
        return True
    return False

print("Example:")
print(is_armstrong(153))
