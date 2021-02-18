import calendar
day = input()
day = day.split()
mm = int(day[0])
dd = int(day[1])
yyyy = int(day[2])

c = calendar.weekday(yyyy,mm,dd)
if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c == 3:
    print("THURSDAY")
elif c == 4:
    print("FRIDAY")
elif c == 5:
    print("SATURDAY")
elif c == 6:
    print("SUNDAY")