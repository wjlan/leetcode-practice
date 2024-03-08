# Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.


# You are not suppose to use the library's sort function for this problem.
# k <= n
# Example
# Example1

# Input: 
# [3,2,2,1,4] 
# 4
# Output: 
# [1,2,2,3,4]
# Example2

# Input: 
# [2,1,1,2,2] 
# 2
# Output: 
# [1,1,2,2,2]


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors or k < 2:
            return colors
        self.sort_helper(colors, 0, len(colors) - 1, 1, k)
    
    def sort_helper(self, colors, index_from, index_to, color_from, color_to):
        if color_from == color_to:
            return

        left, right = index_from, index_to
        mid_color = (color_from + color_to) // 2
        while left <= right:
            while left <= right and colors[left] <= mid_color:
                left += 1
            while left <= right and colors[right] > mid_color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        self.sort_helper(colors, index_from, right, color_from, mid_color)
        self.sort_helper(colors, left, index_to, mid_color + 1, color_to)
