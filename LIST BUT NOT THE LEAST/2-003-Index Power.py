def index_power(ar: list[int], n: int) -> int:
    return -1 if len(ar) < n + 1 else ar[n] ** n

print("Example:")
print(index_power([1, 2, 3], 2))
print(index_power([1, 2, 3], 3))
