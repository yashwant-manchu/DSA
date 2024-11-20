class Solution:
    def pushZerosToEnd(arr):
        # code here
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1
        return arr

arr = [0,0]
print(Solution.pushZerosToEnd(arr))