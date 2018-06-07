#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
Min, Max = [0, n+1]


steps = 0
downflow = upflow = leftflow = rightflow = True
downleft = downright = upleft = upright = True
down = up = right = left = 0
north = south = east = west = 0
northeast = northwest = southeast = southwest = 0

for a0 in range(k):
    rObstacle, cObstacle = input().strip().split(' ')
    rObstacle, cObstacle = [int(rObstacle),int(cObstacle)]

    if rQueen == rObstacle:
        if cObstacle > cQueen:
            if (cObstacle - cQueen - 1) < north or north == 0:
                north = cObstacle - cQueen - 1
            upflow = False
        if cObstacle < cQueen:
            if (cQueen - cObstacle - 1) < south or south == 0:
                south = cQueen - cObstacle - 1
            downflow = False
        # same up and down

    if cQueen == cObstacle:
        if rObstacle > rQueen:
            if (rObstacle - rQueen - 1) < east or east == 0:
                east = rObstacle - rQueen - 1
            rightflow = False
        if rObstacle < rQueen:
            if (rQueen - rObstacle - 1) < west or west == 0:
                west = rQueen - rObstacle - 1
            leftflow = False
        #same right left

    if rObstacle < rQueen and cObstacle < cQueen:
        if rQueen - rObstacle == cQueen - cObstacle:
            if (rQueen - rObstacle - 1) < southwest or southwest == 0:
                southwest = rQueen - rObstacle - 1
            downleft = False
        #left down diagonal

    if rObstacle > rQueen and cObstacle > cQueen:
        if rObstacle - rQueen == cObstacle - cQueen:
            if (rObstacle - rQueen - 1) < northeast or northeast == 0:
                northeast = rObstacle - rQueen - 1
            upright = False
        #right  up diagonal

    if rObstacle < rQueen and cObstacle > cQueen:
        if rQueen - rObstacle == cObstacle - cQueen:
            if (cObstacle - cQueen - 1) < northwest or northwest == 0:
                northwest = cObstacle - cQueen - 1
            upleft = False
        #left up diagonal

    if rObstacle > rQueen and cObstacle < cQueen:
        if rObstacle - rQueen == cQueen - cObstacle:
            if (rObstacle - rQueen - 1) < southeast or southeast == 0:
                southeast += rObstacle - rQueen - 1
            downright = False
        #right down diagonal


if downflow:
    #print ("down")
    for i in range(cQueen-1, Min, -1):
        print(rQueen, i)
        down += 1
if upflow:
    #print ("up")
    for i in range(cQueen+1, Max):
        #print(rQueen, i)
        up += 1

if leftflow:
    #print ("left")
    for i in range(rQueen-1, Min, -1):
        #print(i, cQueen)
        left += 1

if rightflow:
    #print ("right")
    for i in range(rQueen+1, Max):
        #print(i, cQueen)
        right += 1

    # diagonals
    #down left


diadl = diaul = diaur = diadr = Min
rTemp, cTemp = [rQueen, cQueen]
if downleft:
    #print("down left")
    while rTemp > 1 and cTemp > 1:
        rTemp = rTemp-1
        cTemp = cTemp-1
        if rTemp <= Min or cTemp <= Min:
            break
        diadl += 1
        #print(rQueen, cQueen)

    #up left
rTemp, cTemp = [rQueen, cQueen]
if upleft:
    #print("up left")
    while rTemp > 1 and cTemp < Max:
        rTemp = rTemp-1
        cTemp = cTemp+1
        if rTemp <= Min or cTemp >=Max:
            break
        diaul += 1
        #print(rQueen, cQueen)

    #up right
rTemp, cTemp = [rQueen, cQueen]
if upright:
    #print("#up right")
    while rTemp < Max and cTemp < Max:
        rTemp = rTemp+1
        cTemp = cTemp+1
        if rTemp >= Max or cTemp >=Max:
            break
        diaur += 1
        #print(rQueen, cQueen)
    #down right
rTemp, cTemp = [rQueen, cQueen]
if downright:
    #print("#down right")    
    while rTemp < Max and cTemp > 1:
        rTemp = rTemp+1
        cTemp = cTemp-1
        if rTemp >= Max or cTemp <=Min:
            break
        diadr += 1
        #print(rQueen, cQueen)

#print (down, up, right, left)
#print (diadl, diadr, diaul, diaur)
#print (north, northeast, northwest)
#print (south, southeast, southwest)
#print (east, west)
total = down + up + right + left + diadl + diadr + diaul + diaur
total = total + north + northeast + northwest
total = total + south + southeast + southwest
total = total + east + west
print (total)
