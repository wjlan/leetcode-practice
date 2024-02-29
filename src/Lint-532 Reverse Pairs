# '''
# Description
# Two numbers in the array, if the previous number is greater than the following number, then the two numbers form a reverse order pair. Give you an array, find out the total number of reverse order pairs in this array.
# Summary: if a [i] > a [j] and i < j, a [i] and a [j] form a reverse order pair.

# Example
# Example1

# Input:  A = [2, 4, 1, 3, 5]
# Output: 3
# Explanation:
# (2, 1), (4, 1), (4, 3) are reverse pairs
# Example2

# Input:  A = [1, 2, 3, 4]
# Output: 0
# Explanation:
# No reverse pair
# '''

class Solution:
    """
    @param a: an array
    @return: total of reverse pairs
    """
    def reverse_pairs(self, a):
        # write your code here
        tmp = [0 for _ in range(len(a))]
        count = [0]
        self.merge_sort_helper(a, 0, len(a) - 1, tmp, count)
        return count[0]
    
    def merge_sort_helper(self, a, left, right, tmp, count):
        if left >= right:
            return 
        
        mid = (left + right) // 2
        self.merge_sort_helper(a, left, mid, tmp, count)
        self.merge_sort_helper(a, mid + 1, right, tmp, count)
        self.merge(a, left, right, tmp, count)
    
    def merge(self, a, left, right, tmp, count):
        n = right - left + 1
        mid = (left + right) // 2
        i, j = left, mid + 1
        for k in range (n):
            if i <= mid and (j > right or a[i] <= a[j]):
                tmp[k] = a[i]
                i += 1
            else:
                tmp[k] = a[j]
                count[0] += mid - i + 1
                j += 1
        for k in range(n):
            a[left + k] = tmp[k]