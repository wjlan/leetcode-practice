# Given an array of integers, find two non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.


# The subarray should contain at least one number

# Example
# Example 1:

# Input:

# nums = [1, 3, -1, 2, -1, 2]
# Output:

# 7
# Explanation:

# the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
# Example 2:

# Input:

# nums = [5,4]
# Output:

# 9
# Explanation:

# the two subarrays are [5] and [4].


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def max_two_sub_arrays(self, nums: List[int]) -> int:
        # write your code here
        maxSum = float('-inf')
        n = len(nums)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        # calculate from left side to i, max_ending_here at i from left
        left[0] = nums[0]
        max_ending_here = max_so_far = nums[0]
        for i in range(1, n):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_ending_here, max_so_far)
            left[i] = max_so_far

        # calculate from right side to i, max_ending_here at i from right
        right[n - 1] = nums[n - 1]
        max_ending_here = max_so_far = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_ending_here, max_so_far)
            right[i] = max_so_far
        

        for i in range(n - 1):
            maxSum = max(maxSum, left[i] + right[i + 1]) # left subarray until i, right subarray after i + 1 
        
        return maxSum