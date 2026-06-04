#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def position(a, b):
    az0, az1 = a[-1]
    bz0, bz1 = b[-1]

    # z 上面存在交叉，那么不能确定方向
    if not (az1 < bz0 or bz1 < az0):
        return 0

    # z 上没有交叉，大致可以确定顺序，还需要验证x, y
    code = 0
    if az1 < bz0: code = -1
    if bz1 < az0: code = 1
    # check x,y overalpped.
    (ax0, ax1), (ay0, ay1) = a[:2]
    (bx0, bx1), (by0, by1) = b[:2]
    # 如果 x,y 上不重叠，那么两者没有支撑关系
    if ay1 < by0 or by1 < ay0 or bx1 < ax0 or ax1 < bx0:
        return 0
    return code


def falling(objects, names):
    # compare z[0]
    n = len(objects)
    objects.sort(key=lambda x: x[2])
    history = []

    if names:
        print('original position')
        for i in range(n):
            print(f'{names[i]} -> {objects[i]}')

    fall = [set() for _ in range(n)]
    for i in range(n):
        obj = objects[i]

        # 从history里面找到下一个降落的点是哪个
        z = -1
        for r, j in history:
            if z != -1 and r[2][1] != z:
                break
            if position(obj, r) != 0:
                z = r[2][1]
                fall[i].add(j)

        # 如果没有任何降落点，那么就是0.
        if z == -1: z = 0
        rx, ry, rz = obj
        new_rz = (z + 1, rz[1] + z - rz[0] + 1)

        # 按照z[1]进行逆序，这样下一个降落的点就可以找到.
        history.append(((rx, ry, new_rz), i))
        history.sort(key=lambda x: -x[0][2][1])

    if names:
        print('falling position')
        for r, j in history:
            print(f'{names[j]} -> {r}')
        for i in range(n):
            print(f'{names[i]} -> {", ".join([names[x] for x in fall[i]])}')

    ans = set()
    for i in range(n):
        if len(fall[i]) == 1:
            ans.update(fall[i])

    print(f'{n},{len(ans)}')
    return n - len(ans)


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    names = []
    objects = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            if s.find('   <- ') != -1:
                s, name = s.split('   <- ')
                names.append(name)
            a, b = s.split('~')
            a = [int(x) for x in a.split(',')]
            b = [int(x) for x in b.split(',')]
            obj = list(zip(a, b))
            objects.append(obj)

    if not names:
        names = [f'{i}' for i in range(len(objects))]

    # ans = solve(objects, names)
    ans = falling(objects, names)
    print(ans)


if __name__ == '__main__':
    main()
