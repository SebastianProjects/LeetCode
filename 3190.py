class Solution(object):
    def minimumOperations(self, nums):
        return sum([1 for num in nums if num % 3 != 0])