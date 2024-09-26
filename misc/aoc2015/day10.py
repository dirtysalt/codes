#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def main():
    def run(s):
        out = []
        last, cnt = s[0], 1
        for c in s[1:]:
            if c == last:
                cnt += 1
                continue

            out.append(str(cnt))
            out.append(last)
            last, cnt = c, 1

        if cnt:
            out.append(str(cnt))
            out.append(last)
        return ''.join(out)

    s = '1321131112'
    k = 40

    # s = '1'
    # k = 5
    for rep in range(k):
        s2 = run(s)
        if rep < 10:
            print(s, '--->', s2)
        s = s2

    print(len(s))


if __name__ == '__main__':
    main()
