#!/usr/bin/python3
for lowercase in range(ord('a'), ord('z')+1):
    if lowercase != 'e' and lowercase != 'q':
        print(f"{chr(lowercase)}",end="")
