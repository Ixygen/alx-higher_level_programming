#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for item in my_list:
        if idx == my_list.index(item):
            my_list.pop(idx)
            my_list.insert(idx, element)
            return(my_list)
        elif idx < 0:
            return(my_list)
        elif idx >= len(my_list):
            return(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)


print(new_list)
print(my_list)