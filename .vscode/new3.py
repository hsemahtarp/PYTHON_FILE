#HOw to make calendar
def getdate():
    import datetime
    return datetime.datetime.now()

print("The Calendar Will Be Print Here.")
import calendar
y = int(input("Enter Year :- "))
m = int(input("Enter Month :- "))
print(calendar.month(y, m))

print(getdate())
