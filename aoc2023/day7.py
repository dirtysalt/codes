#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


@functools.cache
def get_type(s):
    from collections import Counter
    cnt = Counter(s)
    bucket = [0] * 6
    for c in cnt.values():
        bucket[c] += 1

    def to_value():
        if bucket[5]: return 7
        if bucket[4]: return 6
        if bucket[3] and bucket[2]: return 5
        if bucket[3]: return 4
        if bucket[2] >= 2: return 3
        if bucket[2]: return 2
        return 1

    value = to_value()
    print(s, bucket, value)
    return value


def to_seq(card):
    map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    seq = []
    for c in card:
        if c.isdigit():
            seq.append(int(c))
        else:
            seq.append(map[c])
    return seq


def compare(a, b):
    ta, tb = get_type(a[0]), get_type(b[0])
    if ta != tb:
        return ta - tb
    if a[1] < b[1]: return -1
    if a[1] > b[1]: return 1
    return 0


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    cards = []
    with open(input_file) as fh:
        for s in fh:
            card, bid = s.split()
            seq = to_seq(card)
            bid = int(bid)
            cards.append((card, seq, bid))

    cards.sort(key=functools.cmp_to_key(compare))
    ans = 0
    for i in range(len(cards)):
        ans += cards[i][2] * (i + 1)

    print(cards)
    print(ans)
    return ans


if __name__ == '__main__':
    main()
