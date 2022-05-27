# This code will calculate 
# wether a year is a leap year
# or not

# An extra day is added to the calendar 
# almost every four years as February 29,
# and the day is called a leap day. It corrects 
# the calendar for the fact that our planet takes 
# approximately 365.25 days to orbit the sun. 
# A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years: 
# - The year can be evenly divided by 4, is a leap year, unless:
# - The year can be evenly divided by 100, it is NOT a leap year, unless:
# - The year is also evenly divisible by 400. Then it is a leap year.
#
# source: https://www.timeanddate.com/date/leapyear.html


def leap_year(y):
    try:
        year = int(y)
        if year <= 1900 or year >= 1000000:
            return 'Constraint error'
        elif year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    except:
        return 'Not Int'