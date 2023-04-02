# Task 2
import datetime


def exc(file_name):
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        integer = int(lines.strip())
    except AttributeError:
        print("Attribute error!")
exc("file.txt")

# Task 3

def date(a,b,c,d):

    date1 = datetime.date(year=a, month=b, day=c)
    print(date1)
    date2 = datetime.timedelta(days=d)
    res = date1 + date2
    print(res)
date(2022,4,13,10)

# Task 4
def age(a,b,c):
    now = datetime.datetime.now()
    birth_date = datetime.datetime(year=a, month=b, day=c)
    age_date = now - birth_date
    age_stamp = datetime.datetime.timestamp(now) - datetime.datetime.timestamp(birth_date)

    print(f" This is datetime: {age_date}")
    print(f" This is timestamp: {age_stamp}")
age(2001,5,21)
