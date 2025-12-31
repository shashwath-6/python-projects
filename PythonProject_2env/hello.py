import datetime
"""a = datetime.date(2025,1,15)
print(f"Tommorrow is {a}")"""

a = datetime.datetime.now()
b = datetime.date(2025,1,15)
c= a + datetime.timedelta(days=1)
print(c)
