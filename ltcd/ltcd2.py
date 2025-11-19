"""
My Solution for leetcode 2154. Keep Multiplying Found Values by Two
"""


class Solution:
    def findFinalValue(self,nums,original):
        self.nums = nums
        self.original = original
        while original in nums:
                original = original*2     
        return original

a = Solution()
print(a.findFinalValue([8,19,4,2,15,3],2))