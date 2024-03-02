#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


def solve(s):
    dup = [x * 2 for x in string.ascii_lowercase]
    # adj = [x + y for x, y in zip(string.ascii_lowercase, string.ascii_lowercase[1:])]
    adj = ['ab', 'cd', 'pq', 'xy']
    for x in adj:
        if s.find(x) != -1:
            print('ADJ...', x)
            return 0

    ok = False
    for x in dup:
        if s.find(x) != -1:
            ok = True
            break
    if not ok:
        print("!DUP...")
        return 0

    from collections import Counter
    cnt = Counter()
    for c in s:
        cnt[c] += 1
    num = 0
    for c in 'aeiou':
        num += cnt[c]
    if num < 3:
        print('!VOWELS...')
        return 0

    return 1


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = solve(s)
            print(s, '--->', r)
            ans += r

    print(ans)


if __name__ == '__main__':
    main()
