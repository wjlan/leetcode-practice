
# Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# **Example 1:**

# ```
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# ```

# **Example 2:**




# Dutch National Flag algorithm  最优解
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        i = 0
        j = 0
        for n in range(len(nums)):
            v = nums[n]
            nums[n] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


# QuickSort
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) == 0:
            return
        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = nums[start + (end - start) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)

    
    # Count + 枚举
    class Solution:
        def sortColors(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            if nums is None or len(nums) == 0:
                return
            
            color_cnts = [0] * 3   #一共3个颜色，存放每个颜色出现次数
            for num in nums:        #遍历每个颜色，记录每个颜色出现次数，颜色是有序的，因此每个颜色的代表数字刚好可以用所在list color_cnts的下标表示，不同的下标表示不同颜色
                color_cnts[num] += 1
            
            index = 0     # index用来track nums  
            for i in range(len(color_cnts)):  # 根据每个颜色出现次数，从左到右依次填充0，1，2三种颜色
                cnt = color_cnts[i]  # 获取每一个颜色的cnt，从第一个颜色i=0开始，刚好颜色是有序的数字标记的，就是i
                while cnt > 0:
                    nums[index] = i
                    index += 1
                    cnt -= 1
                    