#Problem Statement: Given an array of integers where each integer is between 1 and
#  n (inclusive), and some integers appear twice while others appear only once, 
# find the duplicate number.

#leetcode:
#Given an array of integers nums containing n + 1 integers where each integer is 
# in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.


class Solution:
    def findDuplicate(self, nums) -> int:
        count =0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)-1):
                if i == j:
                    count+=1
                if count>0:
                    return i
            
Sol = Solution()
a=Sol.findDuplicate([1,2,2,3,4,5])
print(a)