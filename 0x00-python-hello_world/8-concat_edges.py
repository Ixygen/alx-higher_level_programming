#!/usr/bin/python3
str = "python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clever syntax"
str = str.split()
str = str[6:8] + str[13] + str[0]
print(str)
