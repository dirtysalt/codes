#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    n = len(word)
    mh = 0
    for c in word:
        mh = max(mh, h[ord(c) - ord('a')])
    ans = mh * n
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
