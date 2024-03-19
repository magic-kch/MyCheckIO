def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    tmp = [i for i in range(start, cols * rows + start)]
    res = []
    for i in range(1,rows+1):
        if i % 2 != 0:
            res.append(tmp[cols*(i-1):cols * (i-1) + cols])
        else:
            tmp1 = tmp[cols * (i-1) : cols * (i-1) + cols]
            res.append(tmp1[::-1])
    return res

print("Example:")
print(create_zigzag(3, 5))
