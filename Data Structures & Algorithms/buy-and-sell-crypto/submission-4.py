class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = float('inf')
        n = len(prices)
        for i in range(n):
            minp = min(minp, prices[i])
            maxp = max(maxp,prices[i]-minp)
        return maxp