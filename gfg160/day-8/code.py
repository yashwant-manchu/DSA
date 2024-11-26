class Solution:
    def maximumProfit(prices):
        # code here
        
        minValue = prices[0]
        
        res = 0
        
        for i in range(1, len(prices)):
            
            minValue = min(minValue, prices[i])
            
            res = max(res, prices[i] - minValue)
            
        return res

arr = [7, 10, 1, 3, 6, 9, 2]
print(Solution.maximumProfit(arr))