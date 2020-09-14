/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <queue>
#include <tuple>
#include <vector>
using namespace std;

class Solution {
   public:
    typedef tuple<int, int> COO;
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc,
                                  int newColor) {
        vector<vector<int>> im(image);
        char** visited;
        int n = image.size();
        int m = image[0].size();
        visited = new char*[n];
        for (int i = 0; i < n; i++) {
            visited[i] = new char[m]{0};
        }
        int oldColor = image[sr][sc];
        queue<COO> q;
        q.push(make_tuple(sr, sc));
        while (!q.empty()) {
            COO coo = q.front();
            q.pop();
            int r = get<0>(coo);
            int c = get<1>(coo);
            visited[r][c] = 1;
            if ((r + 1) < n && !visited[r + 1][c] && im[r + 1][c] == oldColor) {
                q.push(make_tuple(r + 1, c));
            }
            if ((r - 1) >= 0 && !visited[r - 1][c] &&
                im[r - 1][c] == oldColor) {
                q.push(make_tuple(r - 1, c));
            }
            if ((c + 1) < m && !visited[r][c + 1] && im[r][c + 1] == oldColor) {
                q.push(make_tuple(r, c + 1));
            }
            if ((c - 1) >= 0 && !visited[r][c - 1] &&
                im[r][c - 1] == oldColor) {
                q.push(make_tuple(r, c - 1));
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j]) {
                    im[i][j] = newColor;
                }
            }
        }
        for (int i = 0; i < n; i++) delete visited[i];
        delete[] visited;
        return im;
    }
};
