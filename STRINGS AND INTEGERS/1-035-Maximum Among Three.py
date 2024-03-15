def max_of_three(a: int, b: int, c: int) -> int:
    lst =[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    return int(max(lst))

print("Example:")
print(max_of_three(1, 2, 3))
