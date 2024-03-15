def reverse_digits(num: int) -> int:
    st = str(num)
    if st[0] != "-":
        return int(st[::-1])
    return int("-" + st[:0:-1])

print("Example:")
print(reverse_digits(-32))
