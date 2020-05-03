class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        # dp[i][0] = dp[i-1][1]
        # dp[i][1] = (k-1) * (dp[i-1][0] + dp[i-1][1])
        # dp[0][0] = 0, dp[0][1] = k
        a, b = 0, k
        for i in range(1, n):
            a, b = b, (k-1) * (a + b)
        return a + b
