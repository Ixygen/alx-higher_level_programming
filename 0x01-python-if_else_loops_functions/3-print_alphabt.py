#!/usr/bin/python3
for lowercase in range(ord('a'), ord('z')+1):
    if lowercase == 'e' or lowercase == 'q':
        continue
    print("{:c}".format(lowercase), end="")
