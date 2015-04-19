#!/usr/bin/env python
 
def reverse(text):
    letters = []
    i = len(text)-1
    result = ''
    for char in text:
        letters.append(char)
    while i >=0:
        result = result + letters[i]
        i -= 1
    return result