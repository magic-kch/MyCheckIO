def to_camel_case(name: str) -> str:
    return name.title().replace("_","")

print("Example:")
print(to_camel_case("my_function_name"))
