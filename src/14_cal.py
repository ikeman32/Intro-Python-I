"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

def my_calendar(month = datetime.today().month, year = datetime.today().year):
    '''
    opional user input month, year
    default ouput calendar for curent month and year
    default if only one input will use current month or current year
    if both inputs render calendar for month and year specified
    '''
    print(calendar.month(year, month))

def inputs():
    try:
        month = input('Enter month number ')
        year = input('Enter the year ')

        if month == '' and year == '':
            my_calendar()
        elif month != '' and year == '':
            year = datetime.today().year
            my_calendar(int(month), year)
        elif month == '' and year != '':
            month = datetime.today().month
            my_calendar(month, int(year))
        elif month != '' and year != '':
            my_calendar(int(month), int(year))
    except:
        print('Calendar expects numbers for month and year arguments')



#my_calendar(int(month), int(year))
inputs()
