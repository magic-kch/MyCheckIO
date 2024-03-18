def from_camel_case(name: str) -> str:
    lst = []
    for c in name:
        if c.isupper():
            lst.append("_" + c.lower())
        else:
            lst.append(c)
    return "".join(lst)[1:]

print("Example:")
print(from_camel_case("MyFunctionName"))
