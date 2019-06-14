import datetime

date = datetime.date(*[int(i) for i in input().split(" ")])
date += datetime.timedelta(int(input()))
print(date.year, date.month, date.day)