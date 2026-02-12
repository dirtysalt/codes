/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <vector>
using namespace std;

class Solution {
   public:
    void setZeroes(vector<vector<int>>& matrix) {
        int odd = 78392356;
        for (int r = 0; r < matrix.size(); r++) {
            for (int c = 0; c < matrix[r].size(); c++) {
                if (matrix[r][c] == 0) {
                    for (int k = 0; k < matrix.size(); k++) {
                        if (matrix[k][c] != 0) {
                            matrix[k][c] = odd;
                        }
                    }
                    for (int k = 0; k < matrix[0].size(); k++) {
                        if (matrix[r][k] != 0) {
                            matrix[r][k] = odd;
                        }
                    }
                }
            }
        }
        for (int r = 0; r < matrix.size(); r++) {
            for (int c = 0; c < matrix[r].size(); c++) {
                if (matrix[r][c] == odd) {
                    matrix[r][c] = 0;
                }
            }
        }
    }
};
