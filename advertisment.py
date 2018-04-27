#!/bin/python3
'''
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly  people on social media.

On the first day, half of those 5 people (i.e., floor(5/2) = 2) like the advertisement and each person shares it with 3 of their friends;
the remaining people (i.e., 5 - floor(5/2) - 2 ) delete the advertisement because it doesn't interest them.
So, at the beginning of the second day, floor(5/2) *3 = 2*3 = 6 people receive the advertisement.

On the second day, half of the 6 people who received the advertisement share it with 3 new friends.
So, at the beginning of the third day, floor(6/2) *3 = 3*3 = 9 people receive the advertisement.
The diagram below depicts the advertisement's virality over the first three days (green denotes a person that likes the advertisement and
red denotes a person that disliked and deleted it):

Assume that at the beginning of the ith day, m people received the advertisement, floor(m/2) people like and share it with 3 new friends,
and m - floor(m/2) people dislike and delete it. At the beginning of the i+1 th day, floor(m/2) * 3 people receive the advertisement.

Given an integer, , find and print the total number of people who liked HackerLand Enterprise's advertisement during the first n days.
It is guaranteed that no two people have any friends in common and, after a person shares the advertisement with a friend, the friend always sees it the next day.

'''

import sys
import math

day = int(input().strip())
m = 5
liked = 0
for i in range(day):
    m = math.floor(m/2)
    liked = liked + m
    m = m * 3
        
print (liked)
         
