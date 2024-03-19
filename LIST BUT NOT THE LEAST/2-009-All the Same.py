from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1

print("Example:")
print(all_the_same([1, 1, 1]))
print(all_the_same([1, "a", 1]))
print(all_the_same([1]))
print(all_the_same([]))
