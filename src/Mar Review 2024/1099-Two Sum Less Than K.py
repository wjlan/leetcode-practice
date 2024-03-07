# Given an array nums of integers and integer k, return the maximum sum such that these exists i < j with nums[i] + nums[j] = sum and sum <k. If no i, j exist satisfying this equation, return -1.


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_sum = -1  # Initial to be -1 in case there is no satisfying result
        left, right = 0, n - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < k:
                max_sum = max(max_sum, curr_sum)
                left += 1
            else:
                right -= 1
        return max_sum
