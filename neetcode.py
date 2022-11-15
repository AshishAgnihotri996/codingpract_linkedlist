# class Solution:
#     def twoSum(self,nums,target):
#         prev = {}
#
#         for i , e in enumerate(nums):
#             diff = target- n
#             if diff in prev:
#                 return [prev[diff],i]
#             prev[n] = i
#         return


#stock buy and sell

# class Solution:
#     def maxProfit(self,prices):
#         l ,r = 0,1
#         maxp= 0
#
#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxp = max(maxp,profit)
#             else:
#                 l = r
#             r+=1
#         return maxp


#contains duplicate

# class Solution:
#     def containDuplicate(self,nums):
#         x = set()
#
#         for n in nums:
#             if n in x:
#                 return True
#             x.add(n)
#         return False

#maximum subarray

# class Solution:
#     def maxSubArray(self,nums):
#      maxSub = nums[0]
#      curSum = 0
#
#      for n in nums:
#          if curSum < 0:
#              curSum = 0
#          curSum+=n
#          maxSub = max(maxSub, curSum)
#      return maxSub
#max sub array

# class Solution:
#     def maxsuborb(self,nums):
#         res  = max(nums)
#         curmin, curmax = 1,1
#
#         for n in nums:
#             if n==0:
#                 curmin,curmax = 1,1
#                 continue
#             temp = curmax *n
#             curmax = max(curmax*n,curmin*n)
#             curmin = max(temp,curmin*n)
#             res = max(res,curmax,curmin,n)
#         return res

#minin in rotated in sorted array

# class Solution:
#     def minrotarray(self,nums):
#         res = nums[0]
#         l = 0
#         r = len(nums)-1
#
#         while l < r:
#             if nums[l] < nums[r]:
#                 res = min (res,nums[l])
#                 break
#             m = (l+r)//2
#             res = min (res,nums[m])
#             if nums[m] > nums[l]:
#                 l = m+1
#             else:
#                 r = m-1
#         return res

#search in rotated array
#
# class solution:
#     def searchrotar(self,arr,target):
#         l= 0
#         r = len(arr)-1
#         m = (l+r)//2
#
#         while l <=r:
#             if (target == arr[m]):
#                 return m
#
#             if arr[l] < arr[m]:
#                 if target > arr[m] or target < arr[l]:
#                     l = m+1
#
#                 else:
#                     r = m -1
#
#             else:
#                 if target < arr[m] or target > arr[r]:
#                     r = m -1
#
#                 else:
#                     l = m +1
#         return -1

#coin prbnm dp

def countt(arr,n):
	m = len(arr)
	table = [0 for k in range(n+1)]
	table[0]= 1

	for i in range(0,m):
		for j in range(arr[i],n+1):
			table[j] += table[j - arr[i]]

	return table[n]
arr = [1,2,3,4]
n = 4
x = countt(arr,n)
print(x)

