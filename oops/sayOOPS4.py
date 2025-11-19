nums = [8,15,7,2]
target = 9
l = len(nums)
print(l)

numlist = []
for i in range(0,l):
    for j in range(i+1,l):
        count = 0
        print("Count before inner operation:", count)
        if nums[i] == nums[j]:
            continue
        else:
            count = nums[i] + nums[j]
            print("Combinations:", nums[i], nums[j])
            print("After the operation:", count)
            if count == 9:
                numlist.append(i)
                numlist.append(j)
                continue
            else:
                count = 0

print(numlist)


####


class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        l = len(nums)
        numlist = []
        for i in range(0,l):
            for j in range(i+1,l):
                count = 0
                if nums[i] == nums[j]:
                    continue
                else:
                    count = nums[i] + nums[j]
                    if count == 9:
                        numlist.append(i)
                        numlist.append(j)
                        continue
                    else:
                        count = 0
        return numlist


