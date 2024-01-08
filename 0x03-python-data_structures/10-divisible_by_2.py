#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listdv = []
    for i in my_list:
        if (i % 2) == 0:
            listdv.append(True)
        else:
            listdv.append(False)
    return listdv
