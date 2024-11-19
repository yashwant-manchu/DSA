class Solution:
    def getSecondLargest( arr):
        # Code Here
        n = len(arr)

        arr.sort()

        for i in range(n-2, -1, -1):
            if arr[i] != arr[n-1]:
                return arr[i]
        return -1
input_array = [10,5,10,6]
print(Solution.getSecondLargest(input_array))