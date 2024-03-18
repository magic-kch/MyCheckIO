def from_camel_case(name: str) -> str:
    return "".join(["_" + c.lower() if c.isupper() else c for c in name])[1:]

print("Example:")
print(from_camel_case("MyFunctionName"))
