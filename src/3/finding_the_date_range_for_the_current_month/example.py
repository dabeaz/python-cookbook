from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

first_day, last_day = get_month_range()
a_day = timedelta(days=1)
while first_day < last_day:
    print(first_day)
    first_day += a_day

def daterange(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in daterange(date(2012, 8, 1), date(2012, 8, 11), timedelta(days=1)):
    print(d)

for d in daterange(datetime(2012, 8, 1), datetime(2012, 8, 3), timedelta(minutes=30)):
    print(d)

