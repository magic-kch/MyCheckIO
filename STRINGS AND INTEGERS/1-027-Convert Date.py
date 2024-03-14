import datetime
def convert_date(date: str) -> str:
    try:
        return str(datetime.datetime.strptime(date,'%d/%m/%Y').date())
    except:
        return "Error: Invalid date."

print("Example:")
print(convert_date("01/01/2023"))
