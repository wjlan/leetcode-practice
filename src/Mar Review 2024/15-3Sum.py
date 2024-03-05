# 


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i + 1, len(nums) - 1, -nums[i], res)
        
        return res
        
    def twoSum(self, nums, left, right, target, res):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    res.append([-target, nums[left], nums[right]])
                    last_pair = (nums[left], nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -=1
            else:
                left += 1