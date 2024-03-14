def sum_numbers(text: str) -> int:
    sum = 0
    lst=text.split()
    for x in lst:
        try:
            int(x)
            sum += int(x)
        except ValueError:
            continue
    return sum

print("Example:")
print(sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"))
