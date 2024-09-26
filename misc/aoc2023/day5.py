#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def do_map(seed, mapping):
    for dst, src, size in mapping:
        if src <= seed < src + size:
            return (seed - src) + dst
    return seed


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    seeds = []
    maps = []
    mapping = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            if s.startswith('seeds:'):
                seeds = [int(x) for x in s.split(': ')[1].split()]
            elif s.find('map:') != -1:
                maps.append(mapping)
                mapping = []
            else:
                r = [int(x) for x in s.split()]
                mapping.append(r)
        maps.append(mapping)

    print(maps)
    ans = (1 << 63)
    for seed in seeds:
        dst = seed
        for mapping in maps:
            dst = do_map(dst, mapping)
        ans = min(ans, dst)

    print(ans)


if __name__ == '__main__':
    main()
