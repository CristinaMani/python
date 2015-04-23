#!/usr/bin/env python

mask = 0b1000
def check_bit4(input):
    if (int(bin(input),2) & mask) > 0:
        return "on"
    else:
        return "off"