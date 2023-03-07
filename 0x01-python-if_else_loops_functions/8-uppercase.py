#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # check if character is lowercase
        if ord('a') <= ord(c) <= ord('z'):
            # convert to uppercase using ASCII code
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()
