#!/usr/bin/python3
import functools
def weight_average(my_list=[]):
    aveg = list(map(lambda x: (x[0] * x[1]), my_list))
    all_deno = list(map(lambda x: x[1], my_list))
    sum_averag = functools.reduce(lambda x,y: x+y, aveg)
    sum_deno = functools.reduce(lambda x,y: x+y, all_deno)
    result = sum_averag / sum_deno
    return(result)
