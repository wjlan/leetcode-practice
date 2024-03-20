# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2



# DFS recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDep = 0
        self.dfs(root, 1)
        return self.maxDep

    def dfs(self, root, depth):
        if not root:
            return None
        
        self.maxDep = max(self.maxDep, depth)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
        

# Divide and Conquer
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        if not root:
            return 0  # none为高度0，叶子节点为高度1，end case为走到底就是level 0，叶子为level 1
        
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1