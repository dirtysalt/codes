#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(header, pattern):
    path = []

    def dfs(i):
        if i == len(header):
            p = []
            c = 0
            for x in path:
                if x == '#':
                    c += 1
                else:
                    if c > 0:
                        p.append(c)
                    c = 0
            if c > 0:
                p.append(c)
            # print(path, p)
            return p == pattern

        ans = 0
        if header[i] == '?':
            path.append('.')
            ans += dfs(i + 1)
            path[-1] = '#'
            ans += dfs(i + 1)
            path.pop()
        else:
            path.append(header[i])
            ans += dfs(i + 1)
            path.pop()
        return ans

    return dfs(0)


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            header, pattern = s.split()
            pattern = [int(x) for x in pattern.split(',')]
            r = solve(header, pattern)
            print(header, pattern, r)
            ans += r
    print(ans)
    return ans


if __name__ == '__main__':
    main()
