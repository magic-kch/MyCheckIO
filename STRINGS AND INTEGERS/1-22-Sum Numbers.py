def sum_numbers(text: str) -> int:
    sum_ = 0
    for x in text.split():
        if x.isdigit():
            sum_ += int(x)
    return sum_

print("Example:")
print(sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"))
