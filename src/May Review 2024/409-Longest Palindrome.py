# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.



class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        max_len = 0
        hasOdd = False
        for count in d.values():
            if count % 2 == 0:
                max_len += count
            else:
                max_len += count - 1
                hasOdd = True
        
        return max_len + 1 if hasOdd else max_len

            
    
        