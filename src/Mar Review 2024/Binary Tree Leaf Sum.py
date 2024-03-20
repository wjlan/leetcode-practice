


class Solution:
    '''
    @param root: the root of the binary tree
    @return: An integer
    '''
    def leafSum(self, root):
        self.res = 0
        self.helper(root)
        return self.res
		
    def helper(self, root):
        if root is None:     # DFS走到叶子节点下面None就停止DFS
                return
        if root.left is None and root.right is None:
                self.res += root.val
        self.helper(root.left)
        self.helper(root.right)