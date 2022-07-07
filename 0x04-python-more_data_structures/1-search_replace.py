#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    for i in range(len(my_list)):
        res.append(my_list[i])
    res1 = []
    for i in range(len(res)):
        if res[i] == search:
            res[i] = replace
        res1.append(res[i])
## list comprehension
## return [replace if search == else n  for n in my_list]
    return res1
