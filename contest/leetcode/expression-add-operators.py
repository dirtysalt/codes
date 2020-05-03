#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        mem = {}

        def valid_num(s):
            if not s: return False
            if s[0] == '0' and len(s) >= 2: return False
            return True

        def flip(s):
            s = s.replace('+', '%')
            s = s.replace('-', '+')
            s = s.replace('%', '-')
            return s

        # 只展开含有*的表达式
        def solve_mul(num):
            key = '*.{}'.format(num)
            if key in mem: return mem[key]

            def f(s):
                res = []
                for i in range(1, len(s)):
                    if not valid_num(s[:i]):
                        break
                    v = int(s[:i])
                    rest = f(s[i:])
                    res.extend([(v * x[0], '{}*{}'.format(v, x[1])) for x in rest])
                if valid_num(s):
                    res.append((int(s), s))
                return res

            res = f(num)
            mem[key] = res
            return res

        def solve(num, target):
            key = '+.{}.{}'.format(num, target)
            if key in mem: return mem[key]

            res = []
            # 遍历所有的切分a, b
            for i in range(1, len(num)):
                a = num[:i]
                b = num[i:]

                # 先将a表达式展开只含有*的表达式
                ra = solve_mul(a)
                for va, expa in ra:
                    rest = solve(b, target - va)
                    res.extend([(va + x[0], '{}+{}'.format(expa, x[1])) for x in rest])
                    rest = solve(b, va - target)
                    # 注意这里要做flip, 翻转所有的符号
                    res.extend([(va - x[0], '{}-{}'.format(expa, flip(x[1]))) for x in rest])

            # 当然也可以不进行切分，只包含*表达式
            res_mul = solve_mul(num)
            res.extend([x for x in res_mul if x[0] == target])
            res = list(set(res))
            mem[key] = res
            return res

        res = solve(num, target)
        res = [x[1] for x in res]
        res.sort()
        return res


# class BFSolution:
#     def addOperators(self, num, target):
#         """
#         :type num: str
#         :type target: int
#         :rtype: List[str]
#         """

#         mem = {}

#         def valid_num(s):
#             if not s: return False
#             if s[0] == '0' and len(s) >= 2: return False
#             return True

#         def flip(s):
#             s = s.replace('+', '%')
#             s = s.replace('-', '+')
#             s = s.replace('%', '-')
#             return s

#         def solve(num, mode):
#             key = '{}.{}'.format(mode, num)
#             if key in mem: return mem[key]

#             res = []
#             for i in range(1, len(num)):
#                 a = num[:i]
#                 b = num[i:]

#                 if mode == '+':
#                     ra = solve(a, '+')
#                     rb = solve(b, '+')
#                     for va, expa in ra:
#                         for vb, expb in rb:
#                             res.append((va + vb, '{}+{}'.format(expa, expb)))
#                             res.append((va - vb, '{}-{}'.format(expa, flip(expb))))

#                 if valid_num(a):
#                     va = int(a)
#                     rest = solve(b, '*')
#                     res.extend([(va * x[0], '{}*{}'.format(va, x[1])) for x in rest])

#             if valid_num(num):
#                 res.append((int(num), num))

#             res = list(set(res))
#             mem[key] = res
#             return res

#         res = solve(num, '+')
#         res = list(set([x[1] for x in res if x[0] == target]))
#         res.sort()
#         for k, v in mem.items():
#             for (value, exp) in v:
#                 if eval(exp) != value:
#                     print(exp, value)
#                     break

#         return res


if __name__ == '__main__':
    s = Solution()
    print((s.addOperators('12345', 147)))
    print((s.addOperators('123', 6)))
    print((s.addOperators('232', 8)))
    print((s.addOperators('12345', 6)))
    print((s.addOperators('105', 5)))
    print((s.addOperators('3456237490', 9191)))
    print((s.addOperators('123456789', 45)))
