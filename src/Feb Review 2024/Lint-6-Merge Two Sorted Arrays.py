# Description
# Merge two given sorted ascending integer array A and B into a new sorted   integer array.

# Example
# Example 1:

# Input:

# A = [1]
# B = [1]
# Output:

# [1,1]
# Explanation:

# return array merged.

# Example 2:

# Input:

# A = [1,2,3,4]
# B = [2,4,5,6]
# Output:

# [1,2,2,3,4,4,5,6]


class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        if not a:
            return b
        if not b:
            return a
        
        la = len(a)
        lb = len(b)
        
        res = [0 for _ in range(la + lb)]  # create a array list of a certain size

        i, j = 0, 0
        for k in range(la + lb):
            if i < la and (j >= lb or a[i] <= b[j]):
                res[k] = a[i]
                i += 1
            else:
                res[k] = b[j]
                j += 1
        
        return res