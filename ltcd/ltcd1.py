"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        tarlist = []
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    tarlist.append(i)
                    tarlist.append(j)
        return tarlist
    
a = Solution()
b = a.twoSum([3,2,3],6)
print(b)