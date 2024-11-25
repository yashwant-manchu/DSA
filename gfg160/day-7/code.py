class Solution:
    def maximumProfit(prices):
        # code here
        res = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                res += prices[i] - prices[i-1]
        return res


prices =  [100, 180, 260, 310, 40, 535, 695]
print(Solution.maximumProfit(prices))