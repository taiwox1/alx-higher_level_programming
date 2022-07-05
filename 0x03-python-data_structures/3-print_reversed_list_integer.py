#!/urs/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[len(my_list) - 1 - i])
    for i in new_list:
        print("{:d}".format(i))
