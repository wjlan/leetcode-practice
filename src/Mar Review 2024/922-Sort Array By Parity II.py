# Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half are **even**.

# Sort the array so that whenever `nums[i]` is odd, `i` is **odd**, and whenever `nums[i]` is even, `i` is **even**.

# Return *any answer array that satisfies this condition*.

# **Example 1:**

# ```
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# ```

# **Example 2:**
# Input: nums = [2,3]
# Output: [2,3]


# 同向双指针
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        while even < len(nums) and odd < len(nums):
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2
            while odd < len(nums) and nums[odd] % 2 == 1:
                odd += 2
            if even < len(nums) and odd < len(nums):
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        
        return nums
    

# 相向双指针
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1            # 先partition，左边全部even，右边全部odd
        while even <= odd:
            while even <= odd and nums[even] % 2 == 0:
                even += 1
            while even <= odd and nums[odd] % 2 == 1:
                odd -= 1
            if even <= odd:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 1
                odd -= 1
        
        left, right = 1, len(nums) - 2      # 左右指针从左二和右二开始相向移动每次移动2位，交换奇偶数
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2

        return nums                


