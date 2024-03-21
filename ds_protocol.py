# Evan Kirchstter
# ekirchst@uci.edu
# 59946460

import json
import time
from collections import namedtuple
timestamp = str(time.time())
DataTuple = namedtuple('DataTuple', ['foo', 'baz'])


def extract_json(json_msg: str) -> DataTuple:
    '''
      Call the json.loads function on a json 
      string and convert it to a DataTuple object
      TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    '''
    try:
        json_obj = json.loads(json_msg)
        foo = json_obj['foo']
        baz = json_obj['bar']['baz']
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(foo, baz)


def format_for_json(action_type, user_token=None, message = None, recipient = None):
    formated = None
    if action_type == "1":
        formated = ({
                "token": user_token,
                "directmessage": {
                    "entry": message,
                    "recipient": recipient,
                    'timestamp': timestamp
                }
                })
    elif action_type == '2':
        if not user_token:
            raise ValueError("no user token breh go get that shi")
        formated = ({
                "token": user_token,
                "directmessage": 'new'
                })
    elif action_type == '3':
        if not user_token:
            raise ValueError("go get it bruh bruh")
        formated = ({
                "token": user_token,
                "directmessage": 'all'
                })
    return formated
