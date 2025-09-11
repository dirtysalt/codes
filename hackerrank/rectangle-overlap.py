#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://www.hackerrank.com/contests/cisco-hackathon/challenges/rectangle-overlap

rec1 = [int(x) for x in input().rstrip().split()]
rec2 = [int(x) for x in input().rstrip().split()]

p1 = (rec1[0], rec1[1])
p2 = (rec1[2], rec1[3])
p3 = (rec2[0], rec2[1])
p4 = (rec2[2], rec2[3])

if (p1[0] <= p4[0]) or (p2[0] >= p3[0]) or (p1[1] <= p4[1]) or (p3[1] <= p2[1]):
    print('no overlap')
print('overlap')
