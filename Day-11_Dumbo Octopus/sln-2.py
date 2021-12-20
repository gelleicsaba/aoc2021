#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

with open(os.path.dirname(os.path.abspath(__file__)) + "/input/my-input.txt", "r") as f:
#with open(os.path.dirname(os.path.abspath(__file__)) + "/input/example.txt", "r") as f:
#with open(os.path.dirname(os.path.abspath(__file__)) + "/input/mini-example.txt", "r") as f:
    df = f.readlines()

for x in range(len(df)):
    df[x] = df[x].strip()

ln = len(df)

# state array
m = [None] * ln

#  flashes checks
fl = [None] * ln

for y in range(ln):
    m[y] = [0] * ln
    fl[y] = [False] * ln
    for a in range(ln):
        m[y][a] = int(df[y][a])


def printm():
    for y in range(ln):
        s = ''
        for a in range(ln):
            s = s + str(m[y][a])
        print(s)
    print("")
    return
    


def flash(y, x):
    plus(y, x + 1)
    plus(y, x - 1)

    plus(y-1, x + 1)
    plus(y-1, x)
    plus(y-1, x - 1)

    plus(y+1, x + 1)
    plus(y+1, x)
    plus(y+1, x - 1)
    return

def plus(y, x):
    if x < 0 or x >= ln or y < 0 or y >= ln:
        return

    if m[y][x] == 9 and not fl[y][x]:
        fl[y][x] = True
        m[y][x] = 0
        flash(y, x)

    elif m[y][x] == 9 and fl[y][x]:
        flash(y, x)
    
    elif not fl[y][x]:
        m[y][x] = (m[y][x] + 1)
    
    return

def done():
    n = 0
    for y in range(ln):
        for x in range(ln):
            if m[y][x] == 0:
                n = n + 1
    return n == ln * ln

printm()


sm = 0
while not done():

    for y in range(ln):
        for x in range(ln):
            fl[y][x] = False

    for y in range(ln):
        for x in range(ln):
            plus(y, x)

    sm = sm + 1
    print("After",sm)
    printm()

print("The result:", sm)


