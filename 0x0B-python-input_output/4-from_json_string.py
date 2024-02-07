#!/usr/bin/python3
"""Defining from_json_string function"""


import json


def from_json_string(my_str):
    """Returns JSON string"""
    return json.loads(my_str)
