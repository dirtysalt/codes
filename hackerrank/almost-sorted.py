#!/bin/python3

# Complete the almostSorted function below.
def almostSorted(arr):
    n = len(arr)
    xs = [(i, arr[i]) for i in range(n)]
    xs.sort(key=lambda x: x[1])
    st = []
    for i in range(n):
        if xs[i][0] != i:
            st.append(xs[i][0])

    if len(st) == 0:
        print('yes')
        return

    assert len(st) > 1
    ok = True
    for i in range(1, len(st)):
        if st[i - 1] - st[i] < 0:
            ok = False
            break
    if not ok:
        print('no')
        return

    print('yes')
    a = st[-1] + 1
    b = st[0] + 1
    if len(st) == 2:
        print('swap %d %d' % (a, b))
    else:
        print('reverse %d %d' % (a, b))


if __name__ == '__main__':
    import os
    import sys

    if os.path.exists('tmp.in'):
        sys.stdin = open('tmp.in')
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
