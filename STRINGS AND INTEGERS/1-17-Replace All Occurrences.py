def replace_all(mainText: str, target: str, repl: str) -> str:
    return mainText.replace(target, repl)

print("Example:")
print(replace_all("hello world", "world", "TypeScript"))
