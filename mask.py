#!/usr/bin/env python

mask = 0b1000
def check_bit4(input):
    if (input & mask):
        return "on"
    else:
        return "off"