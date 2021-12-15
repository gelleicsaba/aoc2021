#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

#with open(os.path.dirname(os.path.abspath(__file__)) + "/input/my-input.txt", "r") as f:
with open(os.path.dirname(os.path.abspath(__file__)) + "/input/example.txt", "r") as f:
    df = f.readlines()
for x in range(len(df)):
    df[x] = df[x].strip().replace(" -> ",",")
print(df)

m = []
for x in range(len(df)):
    s = df[x].split(",")
    d = [0] * len(s)
    for y in range(len(d)):
        d[y] = (int)(s[y])
    m.append(d)

print(m)



