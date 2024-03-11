def count_vowels(text: str) -> int:
    return sum(1 for x in text.lower() if x in ('e', 'u', 'i', 'o', 'a'))

print("Example:")
print(count_vowels("Hello"))
