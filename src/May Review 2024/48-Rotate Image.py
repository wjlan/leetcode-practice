# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotate the most outside layer each time, then move into the inside layer
        left, right = 0, len(matrix) - 1
        while left < right:
            #### rotate: rotate (right-left) times for 4 places at a time
            for i in range(right - left):
                top, bottom = left, right
                # save topleft place
                tmp = matrix[top][left + i]
                # move bottomleft to topleft
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottomright to bottomleft
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move topright to bottomright
                matrix[bottom][right - i] = matrix[top + i][right]
                # move topleft to topright
                matrix[top + i][right] = tmp


            left += 1
            right -= 1