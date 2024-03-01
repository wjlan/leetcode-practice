# Given an integer array `nums` and an integer `k`, return *the* `kth` *largest element in the array*.

# Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

# You must solve it in `O(n)` time complexity.

# **Example 1:**

# ```
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# ```

# **Example 2:**


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        # Finding kth largest is equivalent to finding (len(nums) - k)th smallest
        return self.quickSort(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSort(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = max(nums[start + (end - start) // 2], nums[start], nums[end]) # Selecting the maximum element as pivot
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
            return self.quickSort(nums, start, right, k)
        if k >= left:
            return self.quickSort(nums, left, end, k)
        return nums[k] # k刚好夹在left和right中间，一轮partition后的结束状态是right在left左边，可能二者相邻，也可以中间夹一个pivot
