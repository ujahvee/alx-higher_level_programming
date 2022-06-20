#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        total = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print('division by 0')
        except (TypeError):
            print('wrong type')
        except (IndexError):
            print('out of range')
        finally:
            new_list.append(total)
    return (new_list)
