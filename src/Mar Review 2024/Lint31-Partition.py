# Given an array `nums` of integers and an int `k`, partition the array (i.e move the elements in "nums") such that:

# - All elements < *k* are moved to the *left*
# - All elements >= *k* are moved to the *right*

# Return the partitioning index, i.e the first index *i* nums[*i*] >= *k*.

# If all elements in `nums` are smaller than `k`, then return `nums.length`

# 0<=����.�����ℎ<=20000<=*nums*.*length*<=2000

# **Example**

# **Example 1:**

# Input:

# ```
# nums = []
# k = 9

# ```

# Output:

# ```
# 0

# ```

# Explanation:

# Empty array, print 0.

# **Example 2:**

# Input:

# ```
# nums = [3,2,2,1]
# k = 2

# ```

# Output:

# ```
# 1

# ```

# Explanation:

# the real array is[1,2,2,3].So return 1.

# **Challenge**

# Can you partition the array in-place and in *O*(*n*)?


from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return left
        # return right + 1
    
    #结束时的边界是[0, right] [left, len(nums)-1], right在left左边相邻，中间没有任何东西。因为这道题是严格partition小于k在左边和大于等于k在右边