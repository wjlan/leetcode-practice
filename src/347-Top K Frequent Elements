# Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

# Example 1:**

# ```
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# ```

# Example 2:**

# ```
# Input: nums = [1], k = 1
# Output: [1]

# ```

# Constraints:**

# - `1 <= nums.length <= 105`
# - `104 <= nums[i] <= 104`
# - `k` is in the range `[1, the number of unique elements in the array]`.
# - It is **guaranteed** that the answer is **unique**.


class Solution:
    def topKFrequent(self, nums, k):
        # count each num -> map
        res = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1    # -> {1:3, 2:2, 3:1}

        # freq -> [[], []..]
        freq = [[] for _ in range(len(nums) + 1)] # -> [[],[3],[2],[1],[],[],[]]
        for n, c in count.items():
            freq[c].append(n)

        # grab the result
        for i in range(len(nums), -1, -1):  # [[],[3],[2],[1],[],[],[]]
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res