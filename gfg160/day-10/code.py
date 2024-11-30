class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(arr):
        ##Your code here
        
        res = arr[0]
        
        maxEnding = arr[0]
        
        for i in range(1, len(arr)):
            
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            res = max(maxEnding, res)
        
        return res
    
arr = [2, 3, -8, 7, -1, 2, 3]

print(Solution.maxSubArraySum(arr))