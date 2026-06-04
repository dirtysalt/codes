#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(words, sentences):
    # print(words, sentences)
    words = set(words)

    def ok(sentence):
        import functools
        @functools.cache
        def dfs(i):
            if i == len(sentence): return True
            for j in range(i, len(sentence)):
                if sentence[i:j + 1] in words and dfs(j + 1):
                    return True
            return False

        ret = dfs(0)
        dfs.cache_clear()
        return ret

    ans = 0
    for s in sentences:
        if ok(s):
            ans += 1
    return ans


def main():
    input = 'tmp.in'
    sentences = []
    with open(input) as fh:
        words = fh.readline().strip().split(', ')
        for s in fh:
            s = s.strip()
            if not s: continue
            sentences.append(s)

    print(solve(words, sentences))


if __name__ == '__main__':
    main()
