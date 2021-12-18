#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

with open(os.path.dirname(os.path.abspath(__file__)) + "/input/my-input.txt", "r") as f:
#with open(os.path.dirname(os.path.abspath(__file__)) + "/input/example.txt", "r") as f:
    df = f.readlines()
h = 0
d = 0
for x in range(len(df)):
    e = (str)(df[x]).strip().split(' ')
    c = (str)(e[0])
    v = (int)(e[1])
    if (c[0] == 'f'):
        h = h + v
    elif (c[0] == 'd'):
        d = d + v
    elif (c[0] == 'u'):
        d = d - v
print("The result:", (h * d))



