#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(nums):
    last = []
    tmp = nums.copy()
    while True:
        last.append(tmp[-1])
        tmp2 = []
        for i in range(1, len(tmp)):
            tmp2.append(tmp[i] - tmp[i - 1])
        if all((x == 0 for x in tmp2)):
            break
        tmp = tmp2
    return sum(last)


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            nums = [int(x) for x in s.split()]
            r = solve(nums)
            print(nums, '--->', r)
            ans += r
    print(ans)
    return ans


if __name__ == '__main__':
    main()
