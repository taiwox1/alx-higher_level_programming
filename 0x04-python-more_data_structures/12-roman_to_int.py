#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {'M': 1000, 'D': 500, 'c': 100, 'L':50, 'X': 10, 'V': 5, 'I': 1}
    res_rom = {}
    for i, v in enumerate(roman_string):
        res_rom[i] = v
    print(roman_string)
    
    for y in roman_string:
        print(y)
        for i in range(len(roman_string)):
            if (res_rom[i] == y):
                res_rom[i] = roman_dic[y]
    print(res_rom)

