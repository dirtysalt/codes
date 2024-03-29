#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import cProfile
import os.path
import time
from collections import deque, OrderedDict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_tree(xs):
    dq = deque()
    root = TreeNode(xs[0])
    dq.append(root)
    i = 1

    while len(dq):
        h = dq.popleft()

        if i < len(xs):
            if xs[i] is not None:
                l = TreeNode(xs[i])
                h.left = l
                dq.append(l)

        i += 1

        if i < len(xs):
            if xs[i] is not None:
                r = TreeNode(xs[i])
                h.right = r
                dq.append(r)

        i += 1

    return root


def tree_to_list(root):
    res = []
    dq = deque()
    dq.append(root)

    while len(dq):
        root = dq.popleft()
        if root is None:
            res.append(None)
            continue

        res.append(root.val)
        if root.right is not None:
            dq.append(root.left)
            dq.append(root.right)
        elif root.left is not None:
            dq.append(root.left)
    return res


def test_tree_list():
    null = None
    cases = (
        [1, null, 0, 0, 1],
        [1, null, 0, null, 1],

        [1, 0, 1, 0, 0, 0, 1],
        [1, null, 1, null, 1],

        [1, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, null, 1]
    )
    failed = False
    for idx, c in enumerate(cases):
        t = list_to_tree(c)
        res = tree_to_list(t)
        if c != res:
            print('case#{} failed. input = {}, output = {}'.format(idx, c, res))
            failed = True
    if not failed:
        print('all cases passed!!')


ANYTHING = '!!!anything!!!'
EXP = None

PR = cProfile.Profile()
PROFILE = False


def run_test_cases(fn, cases, eqfn=None):
    ok = True
    if eqfn is None:
        eqfn = lambda x, y: x == y

    global PROFILE
    if PROFILE:
        PR.enable()

    for c in cases:
        if isinstance(c, OrderedDict):
            c = tuple(c.values())
        args, exp = c[:-1], c[-1]
        global EXP
        EXP = exp
        start = time.time()
        res = fn(*args)
        end = time.time()
        if exp is not ANYTHING and not eqfn(res, exp):
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
        else:
            print('case passed. %s(!timer = %dms)' % (c, (end - start) * 1000))
    if ok:
        print('all cases passed!!!')

    if PROFILE:
        import pstats, io
        PR.disable()
        s = io.StringIO()
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(PR, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())


def run_simulation_cases(cls, cases, eqfn=None):
    ok = True
    if eqfn is None:
        eqfn = lambda x, y: x == y

    for idx, c in enumerate(cases):
        cmds, args, exp = c
        obj = cls(*args[0])
        res = [None]
        assert cls.__name__ == cmds[0]
        start = time.time()
        for i in range(1, len(cmds)):
            fn = getattr(obj, cmds[i])
            v = fn(*args[i])
            if v != exp[i]:
                print('!DIFF. fn = {}, args = {}, v = {}, exp[{}] = {}'.format(fn, args[i], v, i, exp[i]))
            res.append(v)
        end = time.time()
        if exp is not ANYTHING and not eqfn(res, exp):
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
        else:
            print('case #%d passed(!timer = %dms)' % (idx, (end - start) * 1000))
    if ok:
        print('all cases passed!!!')


def read_cases_from_file(f, size):
    cases = []
    if not os.path.exists(f):
        return cases
    with open(f) as fh:
        c = []
        idx = 0
        for s in fh:
            s = s.strip()
            if not s: continue
            c.append(eval(s))
            idx += 1
            if idx == size:
                cases.append(c)
                idx = 0
                c = []
    return cases


if __name__ == '__main__':
    test_tree_list()
