from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(elements) <= 1 or elements.count(elements[0]) == len(elements)

print("Example:")
print(all_the_same([1, 1, 1]))
print(all_the_same([1, "a", 1]))
print(all_the_same([1]))
print(all_the_same([]))
