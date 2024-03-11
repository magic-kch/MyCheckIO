def count_vowels(text: str) -> int:
    a = 0
    vowels = ('e', 'u', 'i', 'o', 'a',)
    for x in text.lower():
        if x in vowels: a += 1
    return a

print("Example:")
print(count_vowels("Hello"))
