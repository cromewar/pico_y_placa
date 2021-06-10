# Using the language that you feel most proficient in, we’d like you to write a "Pico y Placa" predictor. The inputs should be a license plate number (the full number, not the last digit), a date (as a String), and a time, and the program will return whether or not that car can be on the road. You may use any input and output method you prefer. Although it is not required, we’d love to see the following in your code for extra points:

# Good object-oriented code, avoiding repetition and favoring a consistent organization. You should stick to your chosen language’s semantics, and try to be as consistent as possible.
# Correct usage of version control tools, with a good commit history and incremental software delivery practices.
# Automated testing with any framework or tool of your choice.
# We value candidates that love clean, well-structured code, and that can solve problems in a creative way.

# Please, submit the result to a GitHub, GitLab, or Bitbucket repository and send us the URL within a timeframe of 72 hours. Once we receive this information we’ll ask our technical team to review it and we’ll let you know about the next steps of the process. 

# Note: To develop this application you need to consider the past rules of the Pico&Placa. (Hours: 7:00am - 9:30am / 16:00pm - 19:30). Additional research would be needed to complete the exercise. 

import datetime as dt
from datetime import date
import calendar
import time


def find_day(date):
    '''
    Info: splits the date into day, month and year creating a new datetime object and returning it's day name.
    '''
    try:
        day, month, year = (int(i) for i in date.split('-'))   
        today = dt.date(year, month, day)
        return today.strftime("%A")
    except ValueError as ve:
        print("the format or value/s given is/are incorrect please use it like this (dd-mm-yyyy)")



def get_time(current_time):
    '''
    Info: Splits the time HH:MM given as an string input, verifies if it's a valid time using datetime library with strftime and returns the time as a tuple.
    
    '''
    try:
        hour, minutes = (int(i) for i in current_time.split(':'))
        current = dt.time(hour, minutes)
        current.strftime("%H:%M")
        return (hour, minutes)
    except ValueError as ve:
        print("Please enter a correct Time format HH:MM (ex: 09:30)")


    
    


if __name__ == "__main__":
    # All variables here
    date = '02-08-2004'
    plate = 'AAA0123'
    _week = {
        "Monday": (1,2),
        "Tuesday": (3,4),
        "Wednesday": (5,6),
        "Thursday": (7,8),
        "Friday": (9,0),
        "Saturday": "Free to Go!",
        "Sunday": "Free to Go!"
    }

    print(get_time('09:59'))