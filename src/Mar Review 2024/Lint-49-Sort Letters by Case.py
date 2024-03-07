# **Description**

# Given a string `chars` which contains only letters. Sort it by lower case first and upper case second.

# In different languages, `chars` will be given in different ways. For example, the string `"abc"` will be given in following ways:

# - Java: char[] chars = {'a', 'b', 'c'};
# - Python：chars = ['a', 'b', 'c']
# - C++：string chars = "abc";

# It's *NOT* necessary to keep the original order of lower-case letters and upper case letters.

# **Example**

# **Example 1:**

# Input:

# ```
# chars = "abAcD"

# ```

# Output:

# ```
# "acbAD"

# ```

# Explanation:

# You can also return "abcAD" or "cbaAD" or other correct answers.

# **Example 2:**

# Input:

# ```
# chars = "ABC"

# ```

# Output:

# ```
# "ABC"

# ```

# Explanation:

# You can also return "CBA" or "BCA" or other correct answers.

# **Challenge**

# Do it in one-pass and in-place.


class Solution:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sort_letters(self, chars: List[str]):
        # write your code here
        # partition
        left, right = 0, len(chars) - 1
        while left <= right:
            while left <= right and chars[left].islower():
                left += 1
            while left <= right and chars[right].isupper():
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        return chars
