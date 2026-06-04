#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# http://mnemstudio.org/path-finding-q-learning-tutorial.htm

n_action =  6
n_state = 6

R = []
Q = []
for _ in range(n_state):
    R.append([-1] * n_action)
    Q.append([0] * n_action)

zeros = ((0,4),(1,3),(2,3),(3,1),(3,2),(3,4),(4,0),(4,3),(5,1),(5,4))
for (r,c) in zeros:
    R[r][c] = 0
ones = ((1,5),(4,5),(5,5))
for (r,c) in ones:
    R[r][c] = 100

import pprint
pprint.pprint(R)

n_iter = 100

import random
random.seed(42)
def do_iterate(alpha = 0.1):
    state = random.randint(0, n_state - 1)
    for i in range(100):
    # while state != (n_state - 1):
    # 如果都是在final statet停止的话，那么这一步实际上得不到加强
        actions = [x[0] for x in [x for x in enumerate(R[state]) if x[1] != -1]]
        action = actions[random.randint(0, len(actions) - 1)]
        new_state = action
        reward = R[state][action]
        next_state_max_reward = max(Q[new_state])
        update_delta = (reward + alpha * next_state_max_reward)
        Q[state][action] += update_delta
        state = new_state

for i in range(100):
    do_iterate()
    pprint.pprint(Q)

if True:
# if False:
    state = 0
    while state != (n_state - 1):
        actions = list(enumerate(Q[state]))
        actions.sort(key = lambda x: -x[1])
        action = actions[0][0]
        print(actions)
        print('state = %d, action = %d' % (state, action))
        state = action
