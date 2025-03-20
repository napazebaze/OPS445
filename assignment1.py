#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: a1.py 
Author: Azebaze Ngueya Aime Parfait
Student ID: Napazebaze
The python code in this file (a1_assignment1.py) is original work written by
me.
'''

from datetime import datetime, timedelta

# Function to determine the day of the week for a given date
def day_of_week(year: int, month: int, date: int) -> str:
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

# Function to return the maximum number of days in a given month of a given year
def mon_max(month: int, year: int) -> int:
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# Function to return the next day after a given date
def after(date: str) -> str:
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    
    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        tmp_day = 1
        tmp_month = month + 1
    else:
        tmp_month = month

    if tmp_month > 12:
        tmp_month = 1
        year += 1

    return f"{year}-{tmp_month:02}-{tmp_day:02}"

# Function to check if a year is a leap year
def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to validate a date string
def valid_date(date: str) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to count the number of weekends (Saturdays and Sundays) between two dates
def day_count(start_date: str, stop_date: str) -> int:
    start_obj = datetime.strptime(start_date, "%Y-%m-%d")
    stop_obj = datetime.strptime(stop_date, "%Y-%m-%d")
    
    weekend_count = 0
    current_date = start_obj

    while current_date <= stop_obj:
        if current_date.weekday() in [5, 6]:  # Saturday or Sunday
            weekend_count += 1
        current_date += timedelta(days=1)

    return weekend_count

# Optional: Manual testing block (You can also run CheckA1.py for automated testing)
if __name__ == "__main__":
    # Testing day_of_week function
    print(day_of_week(2023, 1, 23))  # Expected output: 'mon'
    
    # Testing mon_max function
    print(mon_max(2, 2024))  # Expected output: 29 (February in leap year)

    # Testing after function
    print(after('2023-01-01'))  # Expected output: '2023-01-02'

    # Testing leap_year function
    print(leap_year(2024))  # Expected output: True
    print(leap_year(2023))  # Expected output: False

    # Testing valid_date function
    print(valid_date("2024-02-29"))  # Expected output: True
    print(valid_date("2023-02-29"))  # Expected output: False

    # Testing day_count function
    print(day_count("2023-01-01", "2023-01-07"))  # Expected output: 2 (Saturday and Sunday)

