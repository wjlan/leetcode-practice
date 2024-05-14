# Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of* `s`*, and* `false` *otherwise*.

# An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# **Example 1:**

# ```
# Input: s = "anagram", t = "nagaram"
# Output: true

# ```

# **Example 2:**

# ```
# Input: s = "rat", t = "car"
# Output: false

# ```

# **Constraints:**

# - `1 <= s.length, t.length <= 5 * 104`
# - `s` and `t` consist of lowercase English letters.


# Solution 1: convert char to unicode as index in a list
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        return True


# Solution 2: use a dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        for num in count.values():
            if num != 0:
                return False
        
        return True
    