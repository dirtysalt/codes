#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string

adj3 = [''.join(x) for x in zip(string.ascii_lowercase, string.ascii_lowercase[1:], string.ascii_lowercase[2:])]
dup2 = [x + x for x in string.ascii_lowercase]


def check(s):
    for c in s:
        if c in 'iol':
            return False

    ok = False
    for x in adj3:
        if s.find(x) != -1:
            ok = True
            break
    if not ok: return False

    c = 0
    for x in dup2:
        if s.find(x) != -1:
            c += 1
    if c != 2: return False

    return True


def main():
    s = 'vzbxkghb'

    while True:
        if check(s): break
        out = list(s)
        for i in reversed(range(len(out))):
            if out[i] == 'z':
                out[i] = 'a'
            else:
                out[i] = chr(ord(out[i]) + 1)
                break
        s = ''.join(out)

    print(s)


if __name__ == '__main__':
    main()
