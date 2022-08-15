# Imports
from datetime import date
import boto3
import datetime
import os

# Global Variables
THON_date = date(2018,2,16)
# todays_date = datetime.date.today()
todays_date = date(2018,2,15)

# This function will search images from Google and send the first result to your phone
def lambda_handler(event, context):
    days_left = (THON_date-todays_date).days

    if days_left == 0:
        return set_response_in_session("YES! THON is today!!!")
    elif days_left == 1:
        return set_response_in_session("THON is tomorrow!!!")
    elif days_left == 100:
        return set_response_in_session("No, there are " + str(days_left) + " days until THON 2018. Happy 100 days till THON!")
        
    elif days_left > 0:
        return set_response_in_session("No, there are " + str(days_left) + " days until THON 2018.")
    else:
        return set_response_in_session("No, THON is over. See you next year. FTK!")
        

# ---------------------- ALEXA functions -------------------------------
def welcome_response():
    pass

def set_response_in_session(input_string):
    alexa_response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': input_string,
            }
        }
    }
    
    return alexa_response


