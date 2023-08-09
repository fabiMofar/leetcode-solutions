class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}

        for i, num in enumerate(nums):
            if target - num in numbers:
                return numbers[target - num] , i
            numbers[num] = i
            