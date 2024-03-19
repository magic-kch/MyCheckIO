from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    return sorted(sorted(numbers), key=numbers.count, reverse=True)

print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))
print(list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])))
