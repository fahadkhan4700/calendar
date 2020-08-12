import calendar

print(calendar.weekheader(3))
print()

print(calendar.calendar(2050))

day_of_the_week = calendar.weekday(2050, 4, 21)
print(day_of_the_week)

is_leap = calendar.isleap(2024)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2021)
print(how_many_leap_days)

