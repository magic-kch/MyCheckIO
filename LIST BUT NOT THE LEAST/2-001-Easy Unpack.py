def easy_unpack(elements: tuple) -> tuple:
    return tuple([elements[x] for x in [0, 2, -2]])

print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
