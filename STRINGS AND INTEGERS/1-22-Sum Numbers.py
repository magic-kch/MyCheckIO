def sum_numbers(text: str) -> int:
    return sum(int(x) for x in text.split() if x.isdigit())

print("Example:")
print(sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"))
