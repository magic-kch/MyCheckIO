def index_power(ar: list[int], n: int) -> int:
    if len(ar) < n + 1:
        return -1
    return ar[n] ** n

print("Example:")
print(index_power([1, 2, 3], 2))
print(index_power([1, 2, 3], 3))
