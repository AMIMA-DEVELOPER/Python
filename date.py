from datetime import datetime

today = datetime.now()

print("Date:", today.day)
print("Month:", today.strftime("%B"))
print("Year:", today.year)
print("Day:", today.strftime("%A"))
print("calendar")