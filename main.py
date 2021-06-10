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

def input_date():
    '''
    Info: A validation function to verify the correct input of the Date, verifies the length and the format, returns the verified date value.
    '''
    while True:
        date = input("Please enter the date you want to check in this format DD-MM-YYYY (ex: 10-06-2021): \n")
        if len(date) > 10 or len(date) < 10:
            print("the length of the date isn't correct, try again")
            continue
        try:
            day, month, year = (int(i) for i in date.split('-'))   
            dt.date(year, month, day)
            return date
            break
        except ValueError as ve:
            print("the format of the date is incorrect remember to use DD-MM-YYYY format")
            continue

def input_plate():
    '''
    Info: Validates the input of the plate, it's length and if the last number could be transformed to an integer
    '''
    while True:
        plate = input("Enter your plate number using this syntax AAA0123: \n")
        if len(plate) > 7 or len(plate) < 7:
            print("wrong plate length, must be a 7 char plate with this format 'AAA0123'")
            continue
        try:
            int(plate[-1])
            return plate
            break
        except ValueError as ve:
            print("The format of the plate is incorrect, try again")
            continue

def input_time():
    while True:
        time = input('Tell us, what time you want to check, use this format HH:MM (ex: 08:30): \n')
        try:
            hour, minutes = (int(i) for i in time.split(':'))
            dt.time(hour, minutes)
            return time
            break
        except ValueError as ve:
            print("the time format is incorrect, please try again.")
            continue




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

def check_plate(plate):
    '''
    return the last digit as an integer.
    '''
    last_digit = int(plate[-1])
    return last_digit

def _is_pico_y_placa_activated(hour, minutes):
# Note: To develop this application you need to consider the past rules of the Pico&Placa. (Hours: 7:00am - 9:30am / 16:00pm - 19:30). Additional research would be needed to complete the exercise.  
    if hour < 7:
        return False
    elif hour >= 19 and minutes >= 30:
        return False
    elif hour == 9 and minutes >= 30:
        return False
    elif hour > 9 and hour < 16:
        return False
    return True
        
    


def _match_day_with_plate_number(day, week):
    '''
    Info: matchs the the day of the week with it's plate value, returns 10 if it's Saturday or Sunday.
    '''
    if day in week:
        return week.get(day)
    else:
        return (10, 10)





def pico_y_placa(week):
    '''
    Info: returns the information about the Pico & placa pronostic and show a message to the user.
    '''
    date = input_date()
    plate = input_plate()
    time = input_time()
    plate_last_digit = check_plate(plate)
    target_day = find_day(date)
    hour, minutes = get_time(time)
    pico_placa = _is_pico_y_placa_activated(hour, minutes)
    number1, number2 = _match_day_with_plate_number(target_day, week)

    # print(plate_last_digit, target_day, hour, minutes, pico_placa, number1, number2)
    print("Welcome to Pico & Placa Predictor, please take a moment to input the remaining data: ")
    print(f'Hello today is {date}, it\'s a good {target_day}, currently at {time} hours this is your Pico & Placa result for your license plate number {plate}:')
    if plate_last_digit == number1 or plate_last_digit == number2:
        if pico_placa:
            print("Pico & Placa is activated, you can't drive right now, remember not to do it on this hours (7:00am - 9:30am / 16:00pm - 19:30).")
            return 1
        else:
            print("Pico y Placa is not activated at this time, but you have restriction today so remember not to drive on this hours (7:00am - 9:30am / 16:00pm - 19:30).")
            return 2
    else:
        print("Your car does not have Pico y Placa today, you may enjoy the highway at any time.")
        return 0




if __name__ == "__main__":
    _week = {
        "Monday": (1,2),
        "Tuesday": (3,4),
        "Wednesday": (5,6),
        "Thursday": (7,8),
        "Friday": (9,0)
    }
    pico_y_placa(_week)
