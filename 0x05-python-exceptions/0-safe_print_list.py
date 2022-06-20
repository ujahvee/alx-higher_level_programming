#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for idx in range(x):
        try:
            print(f'{my_list[idx]}', end='')

        except (IndexError):
            continue
        
        total += 1
    print()
    return (total)
    