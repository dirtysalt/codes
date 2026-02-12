#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def main():
    nums1, nums2 = [], []
    input = 'tmp.in'
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            a, b = [int(x) for x in s.split()]
            nums1.append(a)
            nums2.append(b)

    nums1 = [(x, idx) for (idx, x) in enumerate(nums1)]
    nums2 = [(x, idx) for (idx, x) in enumerate(nums2)]
    nums1.sort()
    nums2.sort()
    ans = 0
    for (x, idx0), (y, idx1) in zip(nums1, nums2):
        # r = abs(idx0 - idx1)
        r = abs(x - y)
        ans += r
    print(ans)


if __name__ == '__main__':
    main()
