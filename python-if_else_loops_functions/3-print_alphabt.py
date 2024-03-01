#!/usr/bin/python3
i = 0
while i <= 25:
    if i != 4 and i != 16:
        print("{}".format(chr(97 + i)), end='')
    i += 1
