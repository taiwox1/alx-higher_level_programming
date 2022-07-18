#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end ="")
        print("\n")
        return(x)
    except IndexError:
        n = 0;
        print("\n")
        for i in my_list:
            n += 1;
        return(n)
    except TypeError:
        print("TypeError")
