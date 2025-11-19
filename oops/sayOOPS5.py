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