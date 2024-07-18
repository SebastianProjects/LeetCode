class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if nums[i] == i % 10:
                return i
        return -1