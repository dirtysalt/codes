#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def parse_input(s):
    header, s = s.split(':')
    game_id = int(header.split()[1])

    for x in s.split(';'):
        r, g, b = 0, 0, 0
        ss = x.split(', ')
        for s in ss:
            num, color = s.split()
            num = int(num)
            if color == 'red':
                r += num
            elif color == 'green':
                g += num
            elif color == 'blue':
                b += num
        if r <= 12 and g <= 13 and b <= 14:
            pass
        else:
            return 0
    return game_id


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = parse_input(s)
            print(s, '---->', r)
            ans += r
    print('ans = ', ans)
    return ans


if __name__ == '__main__':
    main()
