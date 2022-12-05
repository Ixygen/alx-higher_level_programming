#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = list()
    list = my_list.insert(0, idx)
    for item in my_list:
        if item == my_list.item(0, -1):
            return my_list
        elif item != my_list:
            return my_list
        else:
            return list


new_in_list(my_list, idx, element)
print(new_in_list())
    
