# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.



from collections import defaultdict  # import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        for char in s1:
            count_s1[char] += 1

        left = 0
        for right in range(len(s2)):
            count_s2[s2[right]] += 1
            if (right - left + 1) == len(s1):
                if count_s2 == count_s1:
                    return True
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    del count_s2[s2[left]]
                left += 1

        return False