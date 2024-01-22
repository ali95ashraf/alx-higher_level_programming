#!/usr/bin/python3
def list_division(my_l_1, my_l_2, list_length):
    result = []

    for i in range(list_length):
        try:
            division_result = my_l_1[i] / my_l_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except TypeError:
            print("wrong type")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)

    return result
