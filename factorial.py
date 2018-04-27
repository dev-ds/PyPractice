#!/bin/python3

import sys

'''

Factorial


'''

def fact(n, factorial):
    if n == 1:
        print (factorial)
        return
    factorial = factorial * n
    fact((n-1), factorial)

n = int(input().strip())
factorial = 1
fact(n, factorial)
