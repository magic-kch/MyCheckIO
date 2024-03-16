def is_leap_year(date: int) -> bool:
    return True if (date % 4 == 0) and (date % 100 != 0) or (date % 400 == 0) else False

print("Example:")
print(is_leap_year(2024))
