#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random
from typing import List

import numpy as np

MAX_TAKEN = 5
MAX_ITER = 2000
EXP_W = 0.5
DEBUG_GAME = False
# DEBUG_GAME = True
DEBUG_SIM = False


class Move:
    def __init__(self, taken):
        self.taken = taken

    def __eq__(self, other: 'Move'):
        return self.taken == other.taken

    def __hash__(self):
        return hash(self.taken)

    def __repr__(self):
        return f'(t={self.taken})'


class State:
    def __init__(self, n, player=0):
        self.player = player
        self.n = n

    def get_moves(self):
        return [Move(x) for x in range(1, min(self.n, MAX_TAKEN) + 1)]

    def is_terminal(self):
        return self.n == 0

    def apply_move(self, move: Move):
        return State(self.n - move.taken, 1 - self.player)

    def get_result(self, me):
        assert self.is_terminal()
        if self.player == me:
            return -100
        else:
            return 1

    def __repr__(self):
        return f'(p={self.player},n={self.n})'


class Node:
    def __init__(self, state: State, parent: 'Node', move: 'Move'):
        self.state: State = state
        self.parent: Node = parent
        self.move: Move = move
        self.children: list[Node] = []
        self.expand_moves: set[Move] = set()
        self.visit = 0
        self.value = 0

    def is_fully_expanded(self) -> bool:
        return len(self.children) == len(self.state.get_moves())

    def weights(self, explore_weight: float) -> List[float]:
        weights = [
            (child.value / (child.visit + 1e-6)) + explore_weight * np.sqrt(
                np.log(self.visit + 1) / (child.visit + 1e-6))
            for child in self.children
        ]
        return weights

    def best_child(self, explore_weight: float) -> 'Node':
        weights = self.weights(explore_weight)
        return self.children[np.argmax(weights)]

    def __repr__(self):
        return f'node(state={self.state},move={self.move},visit={self.visit},value={self.value})'


def mcts(init_state: State, iter_max: int, explore_weight: float, rnd: random.Random):
    init_node = Node(init_state, None, None)

    def simulation(state, rnd: random.Random):
        """改进的 Simulation 阶段"""
        while not state.is_terminal():
            moves = state.get_moves()
            # move = max(moves, key=lambda m: m.taken) if rnd.random() > 0.8 else rnd.choice(moves)
            # move = min(moves, key = lambda m: m.taken)
            move = rnd.choice(moves)
            # move = max(moves, key=lambda m: m.taken)
            state = state.apply_move(move)
        return state

    def iterate(root: Node):
        # selection.
        # 如果当前节点不是terminal并且是fully expanded的话，才进行best child筛选
        while root.is_fully_expanded() and not root.state.is_terminal():
            child = root.best_child(explore_weight)
            root = child

        # expansion. 从当前没有fully expanded的节点去扩展一个节点出来
        assert root
        if not root.state.is_terminal():
            assert not root.is_fully_expanded()
            moves = root.state.get_moves()
            for move in moves:
                if move in root.expand_moves: continue
                new_state = root.state.apply_move(move)
                new_child = Node(new_state, root, move)
                root.children.append(new_child)
                root.expand_moves.add(move)
                root = new_child
                break

        # simulation.
        state = root.state
        if not state.is_terminal():
            state = simulation(state, rnd)

        # backprop
        result = state.get_result(init_state.player)
        while root:
            root.visit += 1
            root.value += result
            root = root.parent

    for _ in range(iter_max):
        iterate(init_node)

    best_move = init_node.best_child(0).move

    if DEBUG_SIM:
        print(init_node)
        weights = init_node.weights(0)
        for c, w in zip(init_node.children, weights):
            print(' - ', c, w)
        print(best_move)
    return best_move


def play_game(seed, n):
    rnd = random.Random(seed)
    state = State(n)
    moves = []
    while not state.is_terminal():
        move = mcts(state, MAX_ITER, EXP_W, rnd)
        moves.append(move)
        state = state.apply_move(move)
    return moves


def replay_moves(moves, n):
    state = State(n)
    winner = 1
    for move in moves:
        winner = 1 - winner
        if DEBUG_GAME:
            print(f'Now: {state.n}, Player {state.player} takes {move.taken}')
        state = state.apply_move(move)
    if DEBUG_GAME:
        print(f'Player {"A" if winner == 0 else "B"} wins!')
    return winner


def main():
    for n in range(1, 17 + 1):
        score = [0, 0]
        for seed in range(10):
            moves = play_game(seed, n)
            winner = replay_moves(moves, n)
            score[winner] += 1
        print(n, score)
    #
    # n = 13
    # moves = [1, 5, 1, 1, 5]
    # moves = [Move(x) for x in moves]
    # winner = play_game(moves, n)
    # print(winner)


def test():
    # for seed in range(10):
    for seed in range(5):
        rnd = random.Random(seed)
        init_state = State(5)
        mcts(init_state, MAX_ITER, EXP_W, rnd)


# test()
main()
