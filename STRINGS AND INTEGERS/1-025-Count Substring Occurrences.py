def count_occurrences(main_str: str, sub_str: str) -> int:
    return sum(1 for x in range(len(main_str)-len(sub_str)+1) if main_str[x:len(sub_str)+x].lower() == sub_str.lower())

print("Example:")
print(count_occurrences("hello world hello", "hello"))
