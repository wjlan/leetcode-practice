# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# 打擂台 / sliding window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for price in prices:
            if price > lowest:
                max_profit = max(max_profit, price - lowest)
            else:
                lowest = price

        return max_profit
    

# 同向双指针
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
        
        return max_profit
    

# Kadane算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ending_here = 0
        max_profit = 0
        for i in range(1, len(prices)):
            max_ending_here = max(0, max_ending_here + prices[i] - prices[i - 1])
            max_profit = max(max_profit, max_ending_here)
        return max_profit

    # max_ending_here 指的是ending的那个点为股票卖出点，不管股票买入点是之前的哪个点。Kadane算法就是在每一个扫描点计算以该点为结束点的情况下的结果（即最佳子结构）从而去打擂台。每个位置为终点的计算结果都是基于前一个点为终点的情况来计算