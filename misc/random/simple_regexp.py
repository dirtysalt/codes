#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import time

import io
import os
import re

NFA_DOT_FILE_PATH = 'regexp_nfa'


class State:
    CH_ANY = 0
    CH_SPLIT = 1
    CH_MATCH = 2
    _id = 0
    _states = []

    @classmethod
    def reset(cls):
        cls._id = 0
        cls._states.clear()

    def __init__(self, ch):
        self.id = State._id
        State._id += 1
        self.ch = ch
        self.out0 = None
        self.out1 = None
        State._states.append(self)
        self.name = 's{}'.format(self.id)
        self.matching_id = None

    def patch0(self, s):
        self.out0 = s

    def patch1(self, s):
        self.out1 = s

    def is_matched(self):
        return self.ch == self.CH_MATCH

    def __lt__(self, other):
        idx = id(self)
        idy = id(other)
        return idx < idy


class Frag(object):
    def __init__(self, state: State, patch_fns):
        self.state = state
        self.patch_fns = patch_fns


def make_literal(ch):
    s = State(ch)
    return Frag(s, [s.patch0])


def make_concat(f1: Frag, f2: Frag):
    for fn in f1.patch_fns:
        fn(f2.state)
    return Frag(f1.state, f2.patch_fns)


def make_alter(f1: Frag, f2: Frag):
    s = State(ch=State.CH_SPLIT)
    s.patch0(f1.state)
    s.patch1(f2.state)
    fns = f1.patch_fns + f2.patch_fns
    return Frag(s, fns)


def make_zero_one(f: Frag):
    s = State(ch=State.CH_SPLIT)
    s.patch0(f.state)
    fns = [s.patch1] + f.patch_fns
    return Frag(s, fns)


def make_zero_more(f: Frag):
    s = State(ch=State.CH_SPLIT)
    s.patch0(f.state)
    for fn in f.patch_fns:
        fn(s)
    return Frag(s, [s.patch1])


def make_one_more(f: Frag):
    s = State(ch=State.CH_SPLIT)
    s.patch0(f.state)
    for fn in f.patch_fns:
        fn(s)
    return Frag(f.state, [s.patch1])


def build_nfa(postfix_seq):
    st = []
    for ch in postfix_seq:
        if ch in '.+?*|':
            if ch == '.':
                f1 = st.pop()
                f2 = st.pop()
                st.append(make_concat(f2, f1))
            elif ch == '+':
                f = st.pop()
                st.append(make_one_more(f))
            elif ch == '?':
                f = st.pop()
                st.append(make_zero_one(f))
            elif ch == '*':
                f = st.pop()
                st.append(make_zero_more(f))
            elif ch == '|':
                f1 = st.pop()
                f2 = st.pop()
                st.append(make_alter(f2, f1))
        else:
            st.append(make_literal(ch))

    f = st.pop()
    assert not st
    s = State(ch=State.CH_MATCH)
    for fn in f.patch_fns:
        fn(s)
    return f.state


def dot_to_graph(name, text, type='png'):
    dot_name = name + '.dot'
    graph_name = name + '.' + type

    with open(dot_name, 'w') as fh:
        fh.write(text)

    os.system('gvpack -u {} | dot -T{} -o {}'.format(dot_name, type, graph_name))
    return graph_name


def print_nfa_to_dot(init, name):
    with io.StringIO() as fh:
        fh.write('digraph G {\n')
        fh.write('rankdir=LR\n')
        states = State._states
        for s in states:
            if (s.id + 1) == State._id:
                fh.write('{} [shape=doublecircle]\n'.format(s.name))
            elif s.id == init.id:
                fh.write('{} [shape=circle style=filled fillcolor=red]\n'.format(s.name))
            else:
                fh.write('{} [shape=circle]\n'.format(s.name))

        for st in states:
            if st.ch == State.CH_MATCH:
                continue
            elif st.ch == State.CH_SPLIT:
                fh.write('{} -> {}\n'.format(st.name, st.out0.name))
                fh.write('{} -> {}\n'.format(st.name, st.out1.name))
            else:
                fh.write('{} -> {} [ label="{}"]\n'.format(st.name, st.out0.name, st.ch if st.ch != st.CH_ANY else '?'))
        fh.write('}')
        text = fh.getvalue()

    dot_to_graph(name, text)


class MatchingState:
    _id = 1

    def __init__(self, ss=None):
        self.ss = ss or []
        self.id = MatchingState._id
        MatchingState._id += 1
        self._add_state_stack = []

    def add_state_native(self, s: State):
        # note(yan): 如果matching_id和本次id相同的话，说明已经加入
        #  每个matching state的id是自增的
        if not s or s.matching_id == self.id:
            return
        s.matching_id = self.id
        if s.ch == s.CH_SPLIT:
            self.add_state_native(s.out0)
            self.add_state_native(s.out1)
        self.ss.append(s)

    def step_native_stack(self, last_ms, ch):
        ss = last_ms.ss
        for s in ss:
            if s.ch == ch or s.ch == s.CH_ANY:
                self.add_state_native(s.out0)

    def step_user_stack(self, last_ms, ch):
        ss = last_ms.ss
        for s in ss:
            if s.ch == s.CH_ANY or s.ch == ch:
                self._add_state_stack.append(s.out0)
        self._exhaust_user_stack()

    def add_state_user(self, s: State):
        self._add_state_stack.append(s)
        self._exhaust_user_stack()

    def _exhaust_user_stack(self):
        while self._add_state_stack:
            s = self._add_state_stack.pop()
            if s and s.matching_id != self.id:
                s.matching_id = self.id
                if s.ch == s.CH_SPLIT:
                    self._add_state_stack.append(s.out0)
                    self._add_state_stack.append(s.out1)
                self.ss.append(s)

    # add_state = add_state_user
    # step = step_user_stack

    add_state = add_state_native
    step = step_native_stack

    def empty(self):
        return not self.ss

    def is_matched(self):
        for s in self.ss:
            if s.is_matched():
                return True
        return False


class DFAState:
    def __init__(self, ms: MatchingState):
        ss = ms.ss.copy()
        ss.sort()
        ss = tuple(ss)
        self.ss = ss
        self.next = {}

    def __eq__(self, other):
        return self.ss == other.ss

    def __hash__(self):
        return hash(self.ss)

    def add_next(self, ch, st):
        self.next[ch] = st

    def find_next(self, ch):
        return self.next.get(ch)

    def is_matched(self):
        for s in self.ss:
            if s.is_matched():
                return True
        return False

    def empty(self):
        return not self.ss


class Processor:
    def __init__(self, init_state):
        ms = MatchingState()
        ms.add_state(init_state)
        self.ms: MatchingState = ms
        self.st: DFAState = None
        self.dfa_buffer = []
        self.reset_dfa_buffer()

    def new_dfa_state(self, ms):
        st = DFAState(ms)
        self.dfa_buffer.append(st)
        return st

    def reset_dfa_buffer(self):
        self.dfa_buffer.clear()
        self.st = self.new_dfa_state(self.ms)

    def try_match_with_cache(self, text):
        st = self.st
        for ch in text:
            st2 = st.find_next(ch)
            # note(yan): 没有对应的DFAState
            #  需要使用MatchingState去匹配
            if st2 is None:
                ms = MatchingState(st.ss)
                ms2 = MatchingState()
                ms2.step(ms, ch)
                st2 = self.new_dfa_state(ms2)
                st.add_next(ch, st2)

            if st2.empty():
                return False
            st = st2

        return st.is_matched()

    def try_match(self, text):
        ms = self.ms
        for ch in text:
            ms2 = MatchingState()
            ms2.step(ms, ch)
            if ms2.empty():
                return False
            ms = ms2
        return ms.is_matched()


# ==================== test cases ====================

def test_nfa():
    State.reset()
    postfix_seq = 'abb.+.a.'
    s = build_nfa(postfix_seq)
    print_nfa_to_dot(s, NFA_DOT_FILE_PATH)


# test_nfa()

def test_match():
    State.reset()
    postfix_seq = 'abb.+.a.'
    s = build_nfa(postfix_seq)
    p = Processor(s)

    print(p.try_match('abbba'))
    print(p.try_match('abbbba'))
    print(p.try_match('abbbbba'))
    print(p.try_match('abb'))


# test_match()

def test_match2():
    State.reset()
    import sys
    n = 1000
    sys.setrecursionlimit(min(n, 1000) * 4)
    postfix_seq = 'a?' * n + '.' * (n - 1) + 'a' * n + '.' * n
    s = build_nfa(postfix_seq)
    p = Processor(s)
    print('=====')
    for x in range(3):
        s = time.time()
        for i in range(n - 1, 2 * n):
            res = p.try_match_with_cache('a' * i)
            # print(res)
        e = time.time()
        print('round #{} takes {} ms'.format(x + 1, (e - s) * 1000))


# test_match2()


def test_match3():
    State.reset()
    n = 6
    postfix_seq = 'a?' * n + '.' * (n - 1) + 'a' * n + '.' * n
    s = build_nfa(postfix_seq)
    p = Processor(s)
    print_nfa_to_dot(s, NFA_DOT_FILE_PATH)
    print('===== NFA =====')
    for x in range(3):
        s = time.time()
        for i in range(n - 1, 2 * n):
            res = p.try_match_with_cache('a' * i)
            # print(res)
        e = time.time()
        print('round #{} takes {} ms'.format(x + 1, (e - s) * 1000))

    re_obj = re.compile(r'a?' * n + r'a' * n)
    print('===== re module =====')
    for x in range(3):
        s = time.time()
        for i in range(n - 1, 2 * n):
            res = re_obj.match('a' * i)
            # print(res)
        e = time.time()
        print('round #{} takes {} ms'.format(x + 1, (e - s) * 1000))


# test_match3()


# ==================== leetcode ====================

def build_leetcode_nfa(seq):
    st = []
    for ch in seq:
        if ch == '?':
            st.append(make_literal(State.CH_ANY))
        elif ch == '*':
            f = make_literal(State.CH_ANY)
            st.append(make_zero_more(f))
        else:
            st.append(make_literal(ch))
        if len(st) == 2:
            f1 = st.pop()
            f2 = st.pop()
            st.append(make_concat(f2, f1))

    f = st.pop()
    assert not st
    s = State(ch=State.CH_MATCH)
    for fn in f.patch_fns:
        fn(s)
    return f.state


def test_leetcode_nfa():
    State.reset()
    seq = "*a*b"
    print(seq)
    s = build_leetcode_nfa(seq)
    print_nfa_to_dot(s, NFA_DOT_FILE_PATH)


# test_leetcode_nfa()

class Solution:
    def __init__(self):
        self._cache = {}

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        if p not in self._cache:
            st = build_leetcode_nfa(p)
            pc = Processor(st)
            self._cache[p] = pc
        else:
            pc = self._cache[p]

        return pc.try_match_with_cache(s)


def test_leetcode_solution():
    sol = Solution()
    assert sol.isMatch(s="adceb", p="*a*b")
    assert sol.isMatch(s="acdcb", p="a*c?b") == False

# test_leetcode_solution()
