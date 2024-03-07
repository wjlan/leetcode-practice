# Description
# Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.



# Example
# Example 1:

# Input: nums = [2, 7, 11, 15], target = 24. 
# Output: 5. 
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24
# Example 2:

# Input: nums = [1], target = 1. 
# Output: 0. 


class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left # fix the left, all the left~right number can be paired with the current left
                left += 1 # test next possible left
        
        return count
