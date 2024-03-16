def end_zeros(a: int) -> int:
    cnt = 0
    for x in str(a)[::-1]:
        if x == "0":
            cnt += 1
        else:
            break
    return cnt

print("Example:")
print(end_zeros(10000000))
