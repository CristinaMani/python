#!/usr/bin/env python
 
def median(x):
    s = x.sort()
    n = len(s)
    for av in s:
        if n == 0 or n == 1:
            return x[0]
        elif n % 2 == 0:
            return (x[n/2.0-1] + x[n/2])/2.0
        else:
            return x[(n-1)/2.0]
    median(x)