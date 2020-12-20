/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>>& m = matrix;
        int N = matrix.size();
        for (int r = 0; r < N / 2; r++) {
            int end = N - 1 - r;
            for (int c = r; c < end; c++) {
                int tmp = m[r][c];
                m[r][c] = m[N - 1 - c][r];
                m[N - 1 - c][r] = m[N - 1 - r][N - 1 - c];
                m[N - 1 - r][N - 1 - c] = m[c][N - 1 - r];
                m[c][N - 1 - r] = tmp;
            }
        }
    }
};
