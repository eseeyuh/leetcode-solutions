"""
==================================================
121. Best Time to Buy and Sell Stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
==================================================

PROBLEM:
You are given an array prices where prices[i] is the price
of a given stock on the i-th day. You want to maximize your
profit by choosing a single day to buy one stock and a
different future day to sell it. Return the maximum profit
you can achieve. If no profit is possible, return 0.

APPROACH:
Iterate through prices while tracking the minimum price seen
so far. For each price, calculate the potential profit if we
sold today (current price - min price). Update max profit if
this is better than any previous result. This way we always
buy at the lowest point seen before the current day.

Time complexity:   O(n)
Space complexity:  O(1)
==================================================
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(solution.maxProfit([7, 6, 4, 3, 1]))      # 0
    print(solution.maxProfit([1, 2]))                # 1
