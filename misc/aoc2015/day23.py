#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def evaluate(commands, state):
    offset = 0
    while 0 <= offset < len(commands):
        cmd = commands[offset]
        insts = cmd.split()
        x, r = insts[0], insts[1]
        if x == 'hlf':
            state[r] //= 2
            offset += 1
        elif x == 'tpl':
            state[r] *= 3
            offset += 1
        elif x == 'inc':
            state[r] += 1
            offset += 1
        elif x == 'jmp':
            offset += int(r)
        elif x == 'jie':
            r = r[:-1]
            if state[r] % 2 == 0:
                offset += int(insts[2])
            else:
                offset += 1
        elif x == 'jio':
            r = r[:-1]
            if state[r] == 1:
                offset += int(insts[2])
            else:
                offset += 1
        else:
            raise Exception("Unknown command: " + cmd)


def main():
    test = False
    # test = True

    input_file = 'tmp.in' if test else 'input.txt'
    with open(input_file) as fh:
        commands = [x.strip() for x in fh]

    state = {'a': 0, 'b': 0}
    evaluate(commands, state)
    print(state)


if __name__ == '__main__':
    main()
