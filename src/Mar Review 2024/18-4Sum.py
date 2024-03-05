# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:  
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1
                last_pair = None
                while left < right:
                    currSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if currSum == target:
                        if (nums[left], nums[right]) != last_pair:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                            last_pair = (nums[left], nums[right])
                        left += 1
                        right -= 1
                    elif currSum > target:
                        right -= 1
                    else:
                        left += 1
        
        return res
