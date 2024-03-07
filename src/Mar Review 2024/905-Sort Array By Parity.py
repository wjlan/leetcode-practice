# Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

# Return ***any array** that satisfies this condition*.

# **Example 1:**
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]



class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 0:
                left += 1
            while left <= right and nums[right] % 2 == 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums

