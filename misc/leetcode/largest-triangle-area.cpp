class Solution {
  public:
    double area(int x1, int y1, int x2, int y2, int x3, int y3) {
        int dx1 = x1 - x2;
        int dy1 = y1 - y2;
        int dx2 = x3 - x2;
        int dy2 = y3 - y2;
        int ans = abs(dx1 * dy2 - dx2 * dy1);
        return ans;
    }
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                for (int k = j + 1; k < n; k++) {
                    int x3 = points[k][0], y3 = points[k][1];
                    int res = area(x1, y1, x2, y2, x3, y3);
                    ans = res > ans ? res : ans;
                }
            }
        }
        return ans * 0.5;
    }
};
