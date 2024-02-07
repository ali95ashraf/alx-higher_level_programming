#!/usr/bin/python3
'''task 7 module'''


import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

arglist = list(sys.argv[1:])

try:
    old_data = load_from_json_file('add_item.json')
except Exception:
    old_data = []

old_data.extend(arglist)
save_to_json_file(old_data, 'add_item.json')
