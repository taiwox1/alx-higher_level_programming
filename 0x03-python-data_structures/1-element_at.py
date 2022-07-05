#!/usr/bin/python3

def element_at(my_list, idx):

    if (idx > len(my_list) - 1) or idx < 0:
        return None
    else:
        num_rev = my_list.pop(idx)
        return num_rev
