def from_camel_case(name: str) -> str:
    lst = []
    begin_str = 0
    end_str = 0
    while end_str < len(name) - 1:
        end_str += 1
        if name[end_str].isupper():
            lst.append(name[begin_str:end_str].lower())
            begin_str = end_str
    lst.append(name[begin_str:end_str + 1].lower())
    return "_".join(lst)

print("Example:")
print(from_camel_case("MyFunctionName"))
