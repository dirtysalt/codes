#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def two_lines_cross_point(line1, line2):
    """求解两条线的交点"""
    # https://zhuanlan.zhihu.com/p/138718555
    point_is_exist = False
    x = y = 0
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    if (x2 - x1) == 0:
        k1 = None
        b1 = 0
    else:
        k1 = (y2 - y1) * 1.0 / (x2 - x1)  # 计算k1,由于点均为整数，需要进行浮点数转化
        b1 = y1 * 1.0 - x1 * k1 * 1.0  # 整型转浮点型是关键

    if (x4 - x3) == 0:  # L2直线斜率不存在
        k2 = None
        b2 = 0
    else:
        k2 = (y4 - y3) * 1.0 / (x4 - x3)  # 斜率存在
        b2 = y3 * 1.0 - x3 * k2 * 1.0

    if k1 is None:
        if k2 is not None:
            x = x1
            y = k2 * x1 + b2
            point_is_exist = True
    elif k2 is None:
        x = x3
        y = k1 * x3 + b1
    elif not k2 == k1:
        x = (b2 - b1) * 1.0 / (k1 - k2)
        y = k1 * x * 1.0 + b1 * 1.0
        point_is_exist = True

    return point_is_exist, x, y


def solve(a, b, low, high):
    x0, y0, vx0, vy0 = a
    x1, y1, vx1, vy1 = b
    res = two_lines_cross_point((x0, y0, x0 - vx0, y0 - vy0), (x1, y1, x1 - vx1, y1 - vy1))
    ok, x, y = res
    if ok and low <= x <= high and low <= y <= high:
        # in the past
        if (x - x0) * vx0 < 0: return False
        if (x - x1) * vx1 < 0: return False
        print(a, b, '---->', ok, x, y)
        return True
    return False


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'
    low, high = (7, 27) if test else (200000000000000, 400000000000000)

    objects = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            pos, vec = s.split('@')
            pos = [int(x) for x in pos.split(', ')]
            vec = [int(x) for x in vec.split(', ')]
            objects.append((pos[0], pos[1], vec[0], vec[1]))

    ans = 0
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            if solve(objects[i], objects[j], low, high):
                ans += 1

    print(ans)
    return ans


if __name__ == '__main__':
    main()
