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
import math

def printcal(x):  
  try:
    int(x[1])
  except:
    sys.exit("Error: Enter input in form of: 14_cal.py [month mm] [year yyyy]")
  
  if int(x[1]) < 1 or int(x[1]) > 12:
    sys.exit("Error: Enter a valid month")
  
  currentdatetime = datetime.now()
  currentmonth = int(currentdatetime.strftime("%m"))
  currentyear = int(currentdatetime.strftime("%Y"))
  
  if len(x) == 1 :
  #No input  
    m = currentmonth
    y = currentyear
  elif isinstance(x[1], str) == True:
    m = int(x[1]) 
    if len(x) == 3:
    #Two inputs  
      y = int(x[2])
    else:
    #1 input  
      y = currentyear
  print(calendar.month(y, m))    

x = sys.argv
printcal(x)
