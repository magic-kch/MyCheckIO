def longest_prefix(arr: list[str]) -> str:
    if len(arr) == 1:
        return arr[0]

    for x in range(0, len(arr[0]) - 1):
        if (arr[0][:len(arr[0]) - x] in arr[1]) and (arr[0][:len(arr[0]) - x] in arr[2]):
            return arr[0][:len(arr[0]) - x]
    return ""

print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))
