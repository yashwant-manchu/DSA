# Approach 1
class Solution1:
    def missingPositive(arr):

        arr.sort()

        res = 1

        for i in arr:
            if i == res:
                res+=1
            elif i > res:
                break
        return res

#Time Complexity will be O(n logn)
#Space Complexity will be O(1)

arr = [-3, 1, 1, 3, 4, 7]
print("Approach 1: " , Solution1.missingPositive(arr))


# Approach 2
class Solution2:
     
    def missingPositive(arr):

        n = len(arr)

        vis = [False] * n

        for i in range(n):
            if 0 < arr[i] < n:
                vis[arr[i] - 1] = True
        
        for i in range(1, n+1):
            if not vis[i -1]:
                return i

        return n + 1

#Time Complexity will be O(n)
#Space Complexity will be O(n)

arr = [-3, 1, 1, 3, 4, 7]
print("Approach 2: " , Solution2.missingPositive(arr))


# Approach 3

class Solution3:
    def missingPositive(arr):
        n = len(arr)

        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                temp = arr[i]
                arr[i] = arr[arr[i] - 1]
                arr[temp - 1] = temp
        
        for i in range(1, n+1):
            if i != arr[i-1]:
                return i

        return n + 1

#Time Complexity will be O(n)
#Space Complexity will be O(1)

arr = [-3, 1, 1, 3, 4, 7]
print("Approach 3: " , Solution3.missingPositive(arr))

