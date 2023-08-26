class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]
            else:
                map[num] = i
        return None