def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    if len(str1) > len(str2):
        str2 = str2.ljust(len(str1), "x")
    elif len(str2) > len(str1):
        str1 = str1.ljust(len(str2), "x")

    sum = 0
    for a in range(len(str1)):
        if str1[a] != str2[a]:
            sum += 1
    if sum <= threshold:
        return True
    return False

print("Example:")
print(fuzzy_string_match("apple", "appel", 2))
