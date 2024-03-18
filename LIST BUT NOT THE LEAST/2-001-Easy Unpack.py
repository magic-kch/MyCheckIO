def easy_unpack(elements: tuple) -> tuple:
    return tuple([elements[0], elements[2], elements[-2]])

print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
