#TODO : datetime module
import datetime as dt # we use dt to reduce confusion

current = dt.datetime.now() #datetime - class ; now() - current date and time
#we can't get individual output directly so we will use
year = current.year
month = current.month
day = current.day
print(f"year : {year}\nm"
      f"month : {month}\nday : {day}")
print(current)

date_of_birth = dt.datetime(year=2003 , month=9, day=4, hour=4)
print(date_of_birth)