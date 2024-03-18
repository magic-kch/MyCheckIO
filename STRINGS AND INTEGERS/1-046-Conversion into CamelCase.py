def to_camel_case(name: str) -> str:
    return "".join(x.title() for x in name.split("_"))

print("Example:")
print(to_camel_case("my_function_name"))
