from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    n_set = sorted(list(set(numbers)))
    n_dict = {}
    res = []
    for i in n_set:
        n_dict[i] = numbers.count(i)
    n_dict_sort = dict(sorted(n_dict.items(), key=lambda item: item[1], reverse=True))
    for key, val in n_dict_sort.items():
        res.extend([key] * val)
    return res

print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))
print(list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])))
