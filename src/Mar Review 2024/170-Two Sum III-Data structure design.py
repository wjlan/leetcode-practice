# Design and implement a TwoSum class. It should support the following operations: `add` and `find`.

# `add` - Add the number to an internal data structure.

# `find` - Find if there exists any pair of numbers which sum is equal to

# Example 1:
# add(1); add(3); add(5);
# find(4) // return true
# find(7) // return false


class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.count = {}

    def add(self, number):
        # write your code here
        if number not in self.count:
            self.count[number] = 1
        else:
            self.count[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        return False