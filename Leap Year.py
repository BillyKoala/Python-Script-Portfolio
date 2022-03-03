"""
Billy Knight  - February 2022

This module will calculate whether
or not the year input is a leap year.
"""
import calendar as cal 
 
try: 
 
    year = input("Please Key In Year For Leap Year Check: ") 
 
    if len(year) == 4: 
 
        output = year + " is a leap year." if (cal.isleap(int(year))) else year + " is not a leap year" 
 
        print(output) 
 
    else:

            print("Please enter a 4 digit value.") 
 
except Exception as e: 
    print(e) 
 
finally: 
    pass 