#!/usr/bin/python3
"""Contains the "append_after" function"""


def append_after(filename="", search_string="", new_string=""):
    """Searches for a string in a file and appends a new string after it"""
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
