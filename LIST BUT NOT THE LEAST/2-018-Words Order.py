def words_order(text: str, words: list) -> bool:
    if len(words) != len(set(words)):
        return False
    res = []
    text_lst = text.split()
    for idx, w in enumerate(words):
        for t in text_lst:
            if w == t:
                res.append(text.index(w))
                break
    if len(res) == len(words) :
        return res == sorted(res)
    return False

print("Example:")
print(words_order("hi world im here", ["world", "here"]))
print(words_order("hi world im here", ["wo", "rld"]))
