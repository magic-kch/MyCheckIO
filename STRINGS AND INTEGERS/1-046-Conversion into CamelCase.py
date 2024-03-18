def to_camel_case(name: str) -> str:
    res = ""
    lst = name.split("_")
    for x in lst:
        res += x.title()
    return res

print("Example:")
print(to_camel_case("my_function_name"))
