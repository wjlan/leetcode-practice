# There is an integer array `nums` sorted in ascending order (with **distinct** values).

# Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

# Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

# You must write an algorithm with `O(log n)` runtime complexity.

# **Example 1:**

# ```
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# ```

# **Example 2:**

# ```
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# ```

# **Example 3:**

# ```
# Input: nums = [1], target = 0
# Output: -1

# ```

    

# Best Solution #
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return - 1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return - 1


# 在一个rotated sorted array上切一刀，可以判断出这一刀切在左半部分还是右半部分，这一刀的两边仍然是rotated sorted array，并且至少有一边是单调的，单增数组也是特殊的循环有序数


# Solution 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:     # check both nums is None and nums is empty
            return -1

        index = self.findmin(nums)
        if nums[index] <= target <= nums[-1]:
            return self.binarySearch(nums, index, len(nums) - 1, target)
        return self.binarySearch(nums, 0, index - 1, target)
        

    def findmin(self, nums):
        target = nums[-1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return start
        return end

    def binarySearch(self, nums, start, end, target):
        if end < 0:
            return -1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end 

        return -1


    