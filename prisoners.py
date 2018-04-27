#!/bin/python3

'''
A jail has N prisoners, and each prisoner has a unique id number, S, ranging from 1 to N. 
There are M sweets that must be distributed to the prisoners.

The jailer decides the fairest way to do this is by sitting the prisoners down in a circle (ordered by ascending S), 
and then, starting with some random S, distribute one candy at a time to each sequentially numbered prisoner until 
all M candies are distributed. For example, if the jailer picks prisoner S = 2, then his distribution order would be  
(2, 3, 4, ... n-1, n, 1, 2, 3 ...) until all M sweets are distributed.

But wait—there's a catch—the very last sweet is poisoned! Can you find and print the ID number of the last prisoner 
to receive a sweet so he can be warned?

'''

import sys

def saveThePrisoner(n, m, s):
    if (m+s-1)%n == 0:
        return (n)
    else:
        return (m+s-1)%n
    # Complete this function

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
