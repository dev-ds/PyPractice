#!/bin/python3

import sys

hours = {1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',}
minss = {1:'one',
         2:'two',
         3:'three',
         4:'four',
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine',
         10:'ten',
         11:'eleven',
         12:'twelve',
         13:'thirteen',
         14:'fourteen',
         15:'quarter',
         16:'sixteen',
         17:'seventeen',
         18:'eighteen',
         19:'nineteen',
         20:'twenty',
         21:'twenty one',
         22:'twenty two',
         23:'twenty three',
         24:'twenty four',
         25:'twenty five',
         26:'twenty six',
         27:'twenty seven',
         28:'twenty eight',
         29:'twenty nine',
         30:'half',
         45:'quarter',}

h = int(input().strip())
m = int(input().strip())

if m == 0:
	print ("{0} o' clock".format(hours[h]))
elif m < 30 and m!= 15:
	if m == 1:
		print ("{0} minute past {1}".format(minss[m], hours[h]))
	else:
		print ("{0} minutes past {1}".format(minss[m], hours[h]))
elif m > 30 and m != 45:
	m = 60 - m
	h = h + 1
	if h > 12:
		h = 1
	print ("{0} minutes to {1}".format(minss[m], hours[h]))
elif m in (15, 30):
	print ("{0} past {1}".format(minss[m], hours[h]))
elif m == 45:
    h = h + 1
    if h > 12:
        h = 1
    print ("{0} to {1}".format(minss[m], hours[h]))        
