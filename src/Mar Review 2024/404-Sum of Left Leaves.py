# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 
# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:

# Input: root = [1]
# Output: 0



class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root, False)
        return self.res
    
    def helper(self, root, left):
        if not root:
            return
        
        if not root.left and not root.right and left:
            self.res += root.val
        self.helper(root.left, True)
        self.helper(root.right, False)
