# Given a string `s`, return `true` *if the* `s` *can be palindrome after deleting **at most one** character from it*.

# **Example 1:**

# ```
# Input: s = "aba"
# Output: true

# ```

# **Example 2:**

# ```
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# ```

# **Example 3:**



class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None:
            return None

        left, right = 0, len(s) - 1
        left, right = self.findDifference(s, left, right)
        if left >= right:  # 找完了，不需要去掉任何一个位点，本身就是palindrome
            return True
        
        return self. isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1) # 去掉左边一个或右边一个看看是否是palindrome
    
    def isPalindrome(self, s, left, right):   # 判断palindrome的子函数可以用调用find difference的结果直接判断，避免DRY
        left, right = self.findDifference(s, left, right)
        return left >= right

    def findDifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        
        return left, right