class Solution1:

    def maxProduct(arr):

        n = len(arr)

        currMin = arr[0]

        currMax = arr[0]

        maxProd = arr[0]

        for i in range(1, n):

            temp = max(arr[i], arr[i] * currMin, arr[i] * currMax)

            currMin = min(arr[i], arr[i] * currMin, arr[i] * currMax)

            currMax = temp

            maxProd = max(maxProd, currMax)

        return maxProd

arr = [-2, 6, -3, -10, 0, 2]

print(Solution1.maxProduct(arr))

class Solution2:

    def maxProduct(arr):

        n = len(arr)

        maxProd = float('-inf')

        leftToRight = 1

        rightToLeft = 1

        for i in range(n):

            if leftToRight == 0:
                leftToRight = 1
            if rightToLeft == 0:
                rightToLeft = 1
            
            leftToRight *= arr[i]

            j = n - i - 1

            rightToLeft *= arr[j]

            maxProd = max(maxProd, leftToRight, rightToLeft)

        return maxProd

arr = [-2, 6, -3, -10, 0, 2]

print(Solution2.maxProduct(arr))