class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def maxKilledEnemies(self, grid):
        # write your code here
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        max_kills = 0

        def precompute_by_row(r):
            # from left to right.
            kills = [0] * m
            v = 0
            for c in range(m):
                if grid[r][c] == 'E':
                    v += 1
                elif grid[r][c] == '0':
                    kills[c] += v
                elif grid[r][c] == 'W':
                    v = 0
            # from right to left
            v = 0
            for c in range(m-1, -1, -1):
                if grid[r][c] == 'E':
                    v += 1
                elif grid[r][c] == '0':
                    kills[c] += v
                elif grid[r][c] == 'W':
                    v = 0
            return kills

        def precompute_by_col(c):
            # from left to right.
            kills = [0] * n
            v = 0
            for r in range(n):
                if grid[r][c] == 'E':
                    v += 1
                elif grid[r][c] == '0':
                    kills[r] += v
                elif grid[r][c] == 'W':
                    v = 0
            # from right to left
            v = 0
            for r in range(n-1, -1, -1):
                if grid[r][c] == 'E':
                    v += 1
                elif grid[r][c] == '0':
                    kills[r] += v
                elif grid[r][c] == 'W':
                    v = 0
            return kills

        row_cache = []
        for i in range(n):
            kills = precompute_by_row(i)
            row_cache.append(kills)
        col_cache = []
        for i in range(m):
            kills = precompute_by_col(i)
            col_cache.append(kills)

        # print(row_cache, col_cache)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '0':
                    kills = row_cache[r][c] + col_cache[c][r]
                    if kills > max_kills:
                        max_kills = kills
        return max_kills
