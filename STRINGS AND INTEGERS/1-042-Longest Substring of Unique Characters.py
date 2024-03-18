def longest_substr(s: str) -> int:
    max_ = 0
    for a in s:
        tmp = a
        for b in s:
            if b not in tmp:
                tmp += b
            else:
                if len(tmp) > max_:
                    max_ = len(tmp)
                break
    return max_

print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
print(longest_substr("abcabcbb"), " == 3")
print(longest_substr("bbbbb"), " == 1")
print(longest_substr("pwwkew"), " == 3")
print(longest_substr("abcdef"), " == 6")
print(longest_substr(""), " == 0")
print(longest_substr("au"), " == 2")
print(longest_substr("dvdf"), " == 3")
