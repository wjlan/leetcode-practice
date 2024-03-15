# Description
# Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.


# The value k is a non-negative integer and will no more than the length of the sorted array.
# Length of the given array is positive and will not exceed 
# 1
# 0
# 4
# 10 
# 4
 
# Absolute value of elements in the array will not exceed 
# 1
# 0
# 4
# 10 
# 4
 
# Example
# Example 1:

# Input: A = [1, 2, 3], target = 2, k = 3
# Output: [2, 1, 3]
# Example 2:

# Input: A = [1, 4, 6, 8], target = 3, k = 3
# Output: [4, 1, 6]
# Challenge
# O(logn + k) time


class Solution:
    """
    @param a: an integer aay
    @param target: An integer
    @param k: An integer
    @return: an integer aay
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        result = []
        right = self.upperClosest(a, target)
        left = right - 1
        for _ in range(k):
            if not self.compare(a, left, right, target):
                result.append(a[right])
                right += 1
            else:
                result.append(a[left])
                left -= 1
        
        return result

    def upperClosest(self, a, target):
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < target:
                start = mid
            else:
                end = mid
        
        if a[start] >= target:
            return start
        if a[end] >= target:
            return end
        
        return len(a)

    def compare(self, a, left, right, target):
        if left < 0:
            return False
        if right >= len(a):
            return True
        return target - a[left] <= a[right] - target