# Imports
import json
from utils.bungie import Bungie
from utils.alexa import Alexa

def lambda_handler(event, context):
    
    bungie_util = Bungie()
    alexa_util = Alexa()

    strike_modifiers = bungie_util.get_strike_modifiers()
    strike_modifiers.insert(len(strike_modifiers)-1, 'and')

    strike_modifiers_string = ' '.join(map(str, strike_modifiers))
    strike_response_string = "The strike modifiers today are " + strike_modifiers_string

    return alexa_util.set_response_in_session(strike_response_string)


