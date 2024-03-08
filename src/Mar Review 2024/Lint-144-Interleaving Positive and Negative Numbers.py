# Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

# You are not necessary to keep the original order of positive integers or negative integers.

# **Example**

# ***Example 1***
# Input : [-1, -2, -3, 4, 5, 6]
# Outout : [-1, 5, -2, 4, -3, 6]
# Explanation :  any other reasonable answer.


class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        # write your code here
        neg_count = self.partition(a)
        pos_count = len(a) - neg_count
        left = 1 if neg_count > pos_count else 0
        right = len(a) - 1 if neg_count >= pos_count else len(a) - 2
        self.interleaving(a, left, right)
        

    
    def partition(self, a):
        left, right = 0, len(a) - 1
        while left <= right:
            while left <= right and a[left] < 0:
                left += 1
            while left <= right and a[right] > 0:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1

        return left    

    def interleaving(self, a, left, right):
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 2
            right -= 2   


# partition, count negtives and positives to determine where left and right pointer start, then interleave pairs by moving 2 steps.