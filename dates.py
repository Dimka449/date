import datetime
from array import array
dates = array("i",[3])
cd = datetime.date.today()
current_weekday = cd.weekday()
current_date = datetime.date.today().isoformat()
dates = current_date.split("-")
year = dates[0]
month = dates[1]
date = dates[2]
if(current_weekday == 5 or current_weekday == 6):
    print("выходной")
elif(month == "01" and date == "01"):
    print("выходной")
elif(month == "09" and date == "02"):
    print("выходной")



