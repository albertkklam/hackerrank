# Calendar Module
## https://www.hackerrank.com/challenges/calendar-module/problem
### Python 3.6

import calendar

month, day, year = map(int, input().split(' '))
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
