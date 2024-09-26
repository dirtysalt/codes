#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(data):
    from collections import defaultdict

    # build graph and init values.
    adj = defaultdict(list)
    values = {}
    actions = {}
    for x in data:
        a, b = x.split(' -> ')
        if a.isdigit():
            values[b] = int(a)
            continue

        ss = a.split()
        op = None
        args = []
        for x in ss:
            if x.isupper():
                op = x
                continue
            if x.isdigit():
                args.append(int(x))
            else:
                args.append(x)
                adj[x].append(b)
        actions[b] = (op, args)

    print(actions)
    
    # build backward links.
    back = defaultdict(list)
    from collections import Counter, deque
    ind = Counter()
    for x, ys in adj.items():
        for y in ys:
            ind[y] += 1
            back[y].append(x)

    def evaluate(action):
        op, args = action
        res = []
        for arg in args:
            if isinstance(arg, int):
                res.append(arg)
            else:
                res.append(values[arg])
        args = res

        if op is None: return args[0]
        if op == 'NOT': return 65535 - args[0]
        if op == 'AND': return args[0] & args[1]
        if op == 'OR': return args[0] | args[1]
        if op == 'RSHIFT': return (args[0] >> args[1]) & 65535
        if op == 'LSHIFT':
            return (args[0] << args[1]) & 65535
        else:
            raise Exception(f'Unknown action: {op}, {args}')

    Q = deque()
    for x in values:
        Q.append(x)
    while Q:
        x = Q.popleft()
        if x in actions:
            values[x] = evaluate(actions[x])
        for y in adj[x]:
            ind[y] -= 1
            if ind[y] == 0:
                Q.append(y)

    print(values)
    return values.get('a')


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    with open(input_file) as fh:
        data = [s.strip() for s in fh]
        ans = solve(data)

    print(ans)


if __name__ == '__main__':
    main()
