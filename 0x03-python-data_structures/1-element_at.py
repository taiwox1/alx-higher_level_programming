#!/usr/bin/python3

def element_at(my_list, idx):

    if idx > len(my_list) - 1:
        return None
    num_rev = my_list.pop(idx)
    if num_rev < 0:
        return None
    else:
        return num_rev
