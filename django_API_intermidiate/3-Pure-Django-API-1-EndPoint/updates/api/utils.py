# This file is for validate JSON Data

import json


def is_json(json_data):
    try:
        real_data = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid
