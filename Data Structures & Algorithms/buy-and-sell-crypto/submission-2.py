class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = float('inf')
        n = len(prices)
        dp = [0]*n
        for i in range(n):
            minp = min(minp, prices[i])
            dp[i] = max(dp[i-1],prices[i]-minp)
        return dp[n-1]