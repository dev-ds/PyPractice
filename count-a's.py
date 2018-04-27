#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

count = count_a = 0
for i in s:
    if i == 'a':
        count_a += 1

len_present = n//len(s)
count = (len_present*count_a)
rem = n%len(s)
for i in range(rem):
    if s[i] == 'a':
        count += 1

print (count)
