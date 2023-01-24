#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def test(x):
            depth = [0] * (n + 1)
            from collections import deque
            dq = deque()
            dq.append(x)
            depth[x] = 1
            while dq:
                x = dq.popleft()
                d = depth[x]
                for y in adj[x]:
                    if depth[y] == 0:
                        depth[y] = d + 1
                        dq.append(y)
                    # next level already, or prev level.
                    elif depth[y] != d + 1 and depth[y] != d - 1:
                        return -1
            return max(depth)

        # find connected graph.

        ans = 0
        visited = set()
        for x in range(1, n + 1):
            # find connected graph from x
            # maybe there are many connected graphs.
            def dfs(x, ss):
                ss.add(x)
                for y in adj[x]:
                    if y in ss: continue
                    dfs(y, ss)

            if x in visited: continue
            ss = set()
            dfs(x, ss)

            r = -1
            for x in ss:
                r2 = test(x)
                r = max(r, r2)
            if r == -1: return -1
            ans += r
            visited.update(ss)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]], 4),
    (3, [[1, 2], [2, 3], [3, 1]], -1),
    (92,
     [[67, 29], [13, 29], [77, 29], [36, 29], [82, 29], [54, 29], [57, 29], [53, 29], [68, 29], [26, 29], [21, 29],
      [46, 29], [41, 29], [45, 29], [56, 29], [88, 29], [2, 29], [7, 29], [5, 29], [16, 29], [37, 29], [50, 29],
      [79, 29], [91, 29], [48, 29], [87, 29], [25, 29], [80, 29], [71, 29], [9, 29], [78, 29], [33, 29], [4, 29],
      [44, 29], [72, 29], [65, 29], [61, 29]], 57),
    (448,
     [[366, 183], [81, 44], [242, 91], [69, 97], [39, 373], [391, 386], [342, 349], [136, 229], [393, 386], [60, 185],
      [225, 437], [168, 138], [408, 238], [162, 403], [294, 401], [171, 356], [248, 194], [152, 241], [393, 44],
      [399, 105], [139, 420], [343, 241], [122, 239], [31, 239], [303, 185], [292, 260], [19, 271], [389, 410],
      [212, 83], [219, 44], [393, 335], [68, 62], [417, 118], [150, 437], [200, 183], [257, 359], [329, 426],
      [265, 367], [126, 1], [261, 416], [385, 280], [200, 359], [3, 50], [11, 52], [269, 349], [18, 412], [343, 107],
      [76, 437], [35, 436], [336, 437], [155, 97], [78, 377], [448, 359], [155, 52], [351, 214], [400, 367], [253, 44],
      [102, 214], [218, 4], [6, 91], [10, 412], [323, 107], [294, 44], [395, 236], [87, 185], [115, 447], [100, 386],
      [169, 194], [103, 284], [126, 44], [413, 377], [64, 185], [305, 44], [216, 239], [414, 128], [249, 183],
      [191, 426], [28, 412], [299, 398], [440, 235], [307, 183], [145, 52], [405, 118], [264, 410], [279, 235],
      [181, 437], [102, 236], [22, 118], [347, 105], [325, 437], [423, 284], [80, 273], [66, 401], [161, 377],
      [208, 50], [207, 280], [199, 128], [246, 1], [12, 111], [16, 50], [49, 412], [414, 412], [39, 330], [429, 430],
      [269, 386], [18, 214], [421, 425], [422, 4], [249, 430], [264, 273], [78, 436], [21, 284], [136, 238], [90, 194],
      [289, 62], [414, 185], [427, 52], [39, 258], [35, 107], [301, 185], [422, 436], [75, 377], [6, 398], [159, 262],
      [413, 91], [314, 105], [176, 280], [289, 105], [384, 182], [193, 29], [211, 83], [66, 425], [421, 416],
      [148, 398], [37, 238], [181, 403], [351, 280], [129, 403], [448, 273], [299, 258], [222, 386], [247, 4],
      [269, 83], [33, 349], [78, 118], [353, 280], [340, 185], [360, 352], [438, 194], [99, 335], [396, 235],
      [152, 441], [424, 373], [174, 214], [133, 62], [166, 280], [237, 436], [253, 50], [247, 260], [247, 436],
      [256, 183], [147, 398], [134, 97], [25, 229], [146, 183], [102, 352], [225, 241], [331, 426], [444, 252],
      [369, 401], [46, 262], [274, 52], [244, 62], [423, 241], [440, 252], [60, 426], [201, 335], [47, 386], [186, 91],
      [344, 4], [38, 107], [66, 239], [43, 107], [35, 430], [443, 280], [30, 107], [131, 273], [108, 425], [181, 116],
      [417, 138], [86, 52], [364, 62], [317, 425], [248, 367], [379, 359], [47, 349], [206, 91], [237, 349], [165, 236],
      [339, 262], [384, 185], [75, 367], [3, 271], [149, 401], [294, 447], [19, 437], [53, 403], [245, 52], [122, 29],
      [19, 273], [365, 236], [247, 194], [5, 441], [96, 236], [78, 403], [45, 235], [266, 128], [197, 214], [336, 118],
      [78, 175], [303, 50], [378, 441], [152, 97], [16, 229], [434, 52], [74, 401], [248, 138], [376, 367], [297, 138],
      [353, 412], [311, 273], [66, 273], [257, 116], [165, 352], [302, 284], [327, 359], [161, 420], [370, 425],
      [202, 116], [23, 83], [203, 386], [163, 83], [32, 447], [160, 252], [209, 377], [360, 398], [19, 138], [369, 284],
      [220, 280], [17, 284], [395, 105], [303, 214], [423, 430], [72, 447], [173, 436], [409, 52], [427, 1], [106, 349],
      [390, 403], [435, 412], [104, 111], [332, 280], [316, 52], [380, 352], [154, 386], [86, 280], [133, 373],
      [47, 377], [45, 330], [347, 416], [207, 138], [281, 401], [43, 425], [77, 367], [332, 105], [427, 105],
      [264, 118], [46, 138], [421, 97], [230, 398], [139, 91], [184, 183], [328, 128], [439, 105], [31, 398],
      [165, 425], [31, 241], [369, 118], [147, 447], [340, 373], [37, 349], [146, 359], [96, 349], [306, 238],
      [443, 29], [117, 97], [5, 262], [396, 91], [86, 194], [223, 386], [423, 4], [79, 1], [106, 183], [365, 349],
      [360, 426], [112, 185], [203, 236], [165, 403], [169, 175], [342, 377], [43, 138], [342, 214], [101, 284],
      [148, 238], [247, 118], [197, 420], [15, 356], [161, 185], [313, 416], [3, 410], [409, 273], [134, 4], [369, 437],
      [215, 50], [207, 359], [215, 377], [16, 105], [67, 349], [267, 182], [270, 356], [283, 352], [226, 1], [405, 183],
      [414, 335], [17, 436], [318, 386], [192, 97], [411, 447], [156, 377], [413, 425], [160, 425], [317, 358],
      [371, 91], [320, 105], [432, 189], [253, 236], [147, 273], [85, 1], [347, 330], [270, 29], [2, 377], [342, 138],
      [207, 358], [103, 386], [20, 280], [121, 111], [302, 356], [331, 1], [366, 398], [331, 194], [147, 252]], 181)
]

aatest_helper.run_test_cases(Solution().magnificentSets, cases)

if __name__ == '__main__':
    pass