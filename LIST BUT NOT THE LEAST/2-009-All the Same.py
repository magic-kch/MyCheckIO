from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) <= 1:
        return True
    for i in range(len(elements)):
        if elements[i] != elements[i-1]:
            return False
    return True

print("Example:")
print(all_the_same([1, 1, 1]))
print(all_the_same([1, "a", 1]))
