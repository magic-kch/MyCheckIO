def easy_unpack(elements: tuple) -> tuple:
    new_tup = []
    new_tup.append(elements[0])
    new_tup.append(elements[2])
    new_tup.append(elements[-2])
    return tuple(new_tup)

print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
