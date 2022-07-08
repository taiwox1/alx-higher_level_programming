#!/usr/bin/python3
#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[x] for x in roman_string] + [0]
    rep = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            rep += numbers[i]
        else:
            rep -= numbers[i]

    return rep
#def roman_to_int(roman_string):
#    roman_dic = {'M': 1000, 'D': 500, 'c': 100, 'L':50, 'X': 10, 'V': 5, 'I': 1}
#   res_rom = {}
#  for i, v in enumerate(roman_string):
#     res_rom[i] = v
#    print(roman_string)
#    for y in roman_string:
#print(y)
#        for i in range(len(roman_string)):
#            if (res_rom[i] == y):
#                res_rom[i] = roman_dic[y]
#   print(res_rom)
