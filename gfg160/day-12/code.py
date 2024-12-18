class Solution:
    def circularSubarraySum(arr):
        n = len(arr)
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        maxSum = arr[0]
        minSum = arr[0]

        for i in range(n):

            currMaxSum = max(currMaxSum + arr[i], arr[i])
            maxSum = max(currMaxSum, maxSum)

            currMinSum = min(currMinSum + arr[i], arr[i])
            minSum = min(currMinSum, minSum)

            totalSum += arr[i]

        normalSum = maxSum

        circularSum = totalSum - minSum

        if totalSum == minSum:
            return normalSum
        
        return max(normalSum, circularSum)

arr = [-1,-2,-3] 

print(Solution.circularSubarraySum(arr))
