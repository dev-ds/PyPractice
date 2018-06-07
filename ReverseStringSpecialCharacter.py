# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:18:07 2018

@author: 

Reverse String keeping special characters in same place

"""

def swap(a, b):
    return(b, a)

def main():
    OriStr = str(input('Enter the String: '))
    RevStr = [' '] * len(OriStr)
    if OriStr == OriStr[::-1]:
        print('{} is a Palindrome'.format(OriStr))
    else:
        i = 0; j = len(OriStr)-1
        while True:
            if OriStr[i].isalpha() and OriStr[j].isalpha():
                (RevStr[i], RevStr[j]) = swap(OriStr[i], OriStr[j])
                i += 1
                j -= 1
            elif not OriStr[i].isalpha():
                RevStr[i] = OriStr[i]
                i += 1
            elif not OriStr[j].isalpha():
                RevStr[j] = OriStr[j]
                j -= 1
            if i == j:
                RevStr[i] = OriStr[i]
                break
            elif i > j or j < i:
                break
        Reversed = ''.join(RevStr)
        print(Reversed)

if __name__ == '__main__':
    main()