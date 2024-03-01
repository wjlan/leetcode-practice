
# Find the kth smallest number in an unsorted integer array (`K` start at 1).

# **Example**

# **Example 1:**

# ```
# Input: [3, 4, 1, 2, 5], k = 3
# Output: 3

# ```

# **Example 2:**

# ```
# Input: [1, 1, 1], k = 2
# Output: 1

# ```

# **Challenge**

# An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kth_smallest(self, k: int, nums: List[int]) -> int:
        # write your code here
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)  

    def quickSelect(self, nums, start, end, k):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[left + (right - left) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if k <= right:
            self.quickSelect(nums, start, right, k)
        if k >= left:
            self.quickSelect(nums, left, end, k)

        return nums[k] # k刚好夹在left和right中间，一轮partition后的结束状态是right在left左边，可能二者相邻，也可以中间夹一个pivot
