#!/usr/bin/env python

def foobar(int):
	mask = 0b100
	if (int & mask):
		a = int >> 2
		return a
	else:
		b = int << 1
		return b

print bin(foobar(0b1110))
