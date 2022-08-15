# Imports
import json

class Alexa:
    def set_response_in_session(self, response_string):
        alexa_response = {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': response_string,
                }
            }
        }
        
        return alexa_response