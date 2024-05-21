class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        prev_1 = 1
        prev_2 = 1
        for i in range(2, n + 1):
            curr = prev_1 + prev_2
            prev_1, prev_2 = prev_2, curr
        
        return prev_2
