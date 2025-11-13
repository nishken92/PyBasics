from datetime import date, datetime


d = date(2025,11,11)

print(d)

today = date.today()

print(today)

now = datetime.now()
print(now)

dt = datetime(2025,10,10,10,10,56)
print(dt)

formatted1 = dt.strftime("%Y")
print(formatted1)
formatted2 = dt.strftime("%Y/%B")
print(formatted2)