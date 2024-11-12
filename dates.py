# import datetime
from datetime import date

cd = date.today()
current_weekday = cd.weekday()
current_date = date.today().isoformat()
dates = current_date.split("-")
year = dates[0]
month = dates[1]
day = dates[2]
if current_weekday == 5 or current_weekday == 6:
    print("выходной")
elif month == "01" and day == "01":
    print("выходной")
elif month == "09" and day == "21":
    print("выходной")
else:
    print("всё ещё рабочий")
