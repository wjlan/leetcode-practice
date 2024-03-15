# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.upperclosest(arr, x)
        left = right - 1
        while right - left <= k:
            if self.isLeftCloser(arr, left, right, x):
                left -= 1
            else:
                right += 1
        return arr[left+1: right]

    # find the first one  which is >= x
    def upperclosest(self, arr, x):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] < x:
                start = mid
            else:
                end = mid
        if arr[start] >= x:
            return start
        if arr[end] >= x:
            return end
        return len(arr)

    def isLeftCloser(self, arr, left, right, x):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return x - arr[left] <= arr[right] - x