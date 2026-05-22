/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
   public:
    int findRotateSteps(string ring, string key) {
        int n = ring.size();
        int m = key.size();
        vector<int> dp[2];
        dp[0].resize(n);
        dp[1].resize(n);
        int now = 0;
        for (int i = 0; i < n; i++) {
            dp[now][i] = i;
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int res = INT_MAX;
                bool ok = false;

                for (int step = 0; step < n; step++) {
                    int k = (step + j) % n;
                    if (ring[k] == key[i]) ok = true;
                    if (ok) {
                        res = min(res, dp[now][k] + step);
                    }
                }

                ok = false;
                for (int step = 0; step < n; step++) {
                    int k = (j + n - step) % n;
                    if (ring[k] == key[i]) ok = true;
                    if (ok) {
                        res = min(res, dp[now][k] + step);
                    }
                }

                dp[1 - now][j] = res;
            }
            now = 1 - now;
        }
        int ans = INT_MAX;
        for (int i = 0; i < n; i++) {
            ans = min(ans, dp[now][i]);
        }
        ans += m;
        return ans;
    }
};