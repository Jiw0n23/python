import datetime

now = datetime.datetime.now()

if 1 <= now.month <=2 or now.month == 12:
    print("이번 달은 겨울로 {}월입니다".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 여름으로 {}월입니다".format(now.month))