#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _checkdiv = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            _checkdiv.append(True)
        else:
            _checkdiv.append(False)

    return (_checkdiv)
