#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq


def build_graph(rules):
    actions = {}
    from collections import defaultdict
    forward = defaultdict(list)
    backward = defaultdict(list)
    for r in rules:
        a, b = r.split(' -> ')
        act = '-'
        if a != 'broadcaster':
            act, a = a[0], a[1:]
        actions[a] = act
        for c in b.split(', '):
            forward[a].append(c)
            backward[c].append(a)

    return forward, backward, actions


NO_SIGNAL = -1


class State:
    def __init__(self, name, act, inputs):
        self.name = name
        self.inputs = {x: 0 for x in inputs}
        self.value = 0
        self.act = act

    def emit(self, src, p):
        # print(f'{src} -{"low" if p == 0 else "high"}-> {self.name}')
        act = self.act
        if act == '%':
            if p == 1: return NO_SIGNAL
            self.value = 1 - self.value
            return self.value
        if act == '&':
            self.inputs[src] = p
            # todo: optimize
            if all(x == 1 for x in self.inputs.values()):
                return 0
            return 1
        return NO_SIGNAL


def solve(forward, backward, actions):
    nodes = set(forward.keys()) | set(backward.keys())
    pulses = [0] * 2
    states = {x: State(x, actions.get(x, '-'), backward[x]) for x in nodes}

    def run():
        Q = []

        src = 'broadcaster'
        # print(f'button -low-> {src}')
        pulses[0] += 1  # to broadcaster
        for x in forward[src]:
            pulses[0] += 1
            Q.append((1, 0, x, src))

        while Q:
            t, p, x, src = heapq.heappop(Q)
            po = states[x].emit(src, p)
            if po == NO_SIGNAL: continue
            for y in forward[x]:
                pulses[po] += 1
                heapq.heappush(Q, (t + 1, po, y, x))

    rep = 1000
    for _ in range(rep):
        run()

    print(pulses)
    return pulses[0] * pulses[1]


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'
    rules = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            rules.append(s)
    forward, backward, actions = build_graph(rules)
    ans = solve(forward, backward, actions)
    print(ans)


if __name__ == '__main__':
    main()
