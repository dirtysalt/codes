#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        cache = {}

        def play(total, state):
            key = '{}.{}'.format(total, state)
            if key in cache:
                return cache[key]

            res = 'draw'
            lose = False
            for i in range(maxChoosableInteger - 1, -1, -1):
                if (state >> i) & 0x1:
                    value = i + 1
                    if value >= total:
                        res = 'win'
                        break

                    new_state = state & (~(1 << i))
                    sub = play(total - value, new_state)
                    if sub == 'lose':
                        res = 'win'
                        break
                    elif sub == 'win':
                        lose = True
            if res == 'draw' and lose:
                res = 'lose'
            cache[key] = res
            return res

        state = (1 << (maxChoosableInteger + 1)) - 1
        res = play(desiredTotal, state)
        # print(res)
        return res == 'win'


if __name__ == '__main__':
    s = Solution()
    print(s.canIWin(10, 11))
    print(s.canIWin(10, 20))
    print(s.canIWin(5, 50))
    print(s.canIWin(18, 188))
