# '''
# Description
# Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

# Example
# Example1:

# Input: [3, 2, 1, 4, 5], 
# Output: [1, 2, 3, 4, 5].
# Example2:

# Input: [2, 3, 1], 
# Output: [1, 2, 3].
# '''

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        # write your code here
    
    # Merge Sort
        tmp = [0 for _ in range(len(a))]
        self.merge_sort_helper(a, 0 , len(a) - 1, tmp)
    
    def merge_sort_helper(self, a, left, right, tmp):
        if left >= right:     # 递归的出口
            return

        mid = (left + right) // 2
        self.merge_sort_helper(a, left, mid, tmp)
        self.merge_sort_helper(a, mid + 1, right, tmp)
        self.merge(a, left, right, tmp)
    
    def merge(self, a, left, right, tmp):
        n = right - left + 1
        mid = (left + right) // 2
        i, j = left, mid + 1
        for k in range(n):
            if i <= mid and (j > right or a[i] < a[j]):
                tmp[k] = a[i]
                i += 1
            else:
                tmp[k] = a[j]
                j += 1

        for k in range(n):
            a[left + k] = tmp[k]
    

    # merge sort 最优化模版
    #       time: O(nlogn)
    #       space: O(n)
            


    # QuickSort
        self.quick_sort_helper(a, 0, len(a) - 1)
    
    def quick_sort_helper(self, a, start, end):
        if start >= end:
            return 
        
        left, right = start, end
        pivot = a[(left + right) // 2]

        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        
        self.quick_sort_helper(a, start, right)
        self.quick_sort_helper(a, left, end)
            
    # Quick sort 最优化模版
    #       time: O(nlogn)
    #       space: O(1)
        