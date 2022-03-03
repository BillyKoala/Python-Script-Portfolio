"""
Billy Knight – March 2022

This module will look for two specific numbers
In a number array and sum them up individually.
"""

def count_ratings(): 

    try: 
        ratings=[4,5,3,4,5,3,5,3,1,3,1] 
 
        count_ones = 0 
        count_fives = 0

        for num in ratings: 
 
            count_ones += 1 if num == 1 else 0 
            count_fives += 1 if num == 5 else 0 

        print("Num Of 1\'s = {}\nNum Of 5\'s = {}".format(str(count_ones), str(count_fives)))
 
    except Exception as e: 
        print(e) 
 
    finally: 
        pass 

count_ratings() 