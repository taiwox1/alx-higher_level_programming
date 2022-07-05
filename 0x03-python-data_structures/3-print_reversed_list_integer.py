#!/urs/bin/python3
my_list = [2,3,4,5,6]
new_list = []
for i in range(len(my_list)):
    new_list.append(my_list[len(my_list) - 1 - i])
for i in new_list:
    print("{:d}".format(i))
