/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <condition_variable>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <mutex>
#include <string>
#include <thread>
#include <vector>

using namespace std;

char dp[101][55][55][4];
char can[101][55][55][4];

class Solution {
   public:
    bool escapeMaze(vector<vector<string>>& maze) {
        int T = maze.size();
        int N = maze[0].size();
        int M = maze[0][0].size();
        memset(dp, 0, sizeof(dp));
        memset(can, 0, sizeof(can));
        dp[0][0][0][0] = 1;

        for (int t = 0; t < T - 1; t++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    for (int st = 0; st < 4; st++) {
                        char v = dp[t][i][j][st];
                        if (st & 0x2) {
                            v |= can[t][i][j][st];
                        }
                        if (!v) continue;

                        for (int dx = -1; dx <= 1; dx++) {
                            for (int dy = -1; dy <= 1; dy++) {
                                if (dx != 0 && dy != 0) continue;
                                int x = i + dx;
                                int y = j + dy;
                                if (!(x >= 0 && x < N && y >= 0 && y < M))
                                    continue;
                                if (maze[t + 1][x][y] == '.') {
                                    dp[t + 1][x][y][st] = 1;
                                    continue;
                                }
                                if ((st & 0x1) == 0) {
                                    dp[t + 1][x][y][st | 0x1] = 1;
                                }
                                if ((st & 0x2) == 0) {
                                    can[t + 1][x][y][st | 0x2] = 1;
                                }
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    for (int st = 0; st < 4; st++) {
                        if (st & 0x2) {
                            can[t + 1][i][j][st] |= can[t][i][j][st];
                        }
                    }
                }
            }
        }
        for (int st = 0; st < 4; st++) {
            if (dp[T - 1][N - 1][M - 1][st]) {
                return true;
            }
        }
        return false;
    }
};

int main() { return 0; }
