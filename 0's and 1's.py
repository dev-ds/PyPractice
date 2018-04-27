#!/bin/python3

import sys

'''

You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are counted as two different teams.

Input Format

The first line contains two integers, N and M, separated by a single space, where N represents the number of people, and M represents the number of topics. N lines follow.
Each line contains a binary string of length M. If the ith line's jth character is 1, then the ith person knows the jth topic; otherwise, he doesn't know the topic.

Output Format

On the first line, print the maximum number of topics a 2-person team can know. 
On the second line, print the number of 2-person teams that can know the maximum number of topics.

Sample Input

4 5
10101
11100
11010
00101
Sample Output

5
2
'''

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
team = [0]*(m+1)
topic_i = 0
maxtop = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

team = [0]*(m+1)
for i in range(0, len(topic)-1):
    for j in range(i+1, len(topic)):
        top_count = 0
        for k, l in zip(topic[i], topic[j]):
            if k == '1' or l == '1':
                top_count += 1
        if top_count > maxtop:
            maxtop = top_count
        if top_count == maxtop:
            team[top_count] += 1

print (maxtop)
print (team[maxtop])
