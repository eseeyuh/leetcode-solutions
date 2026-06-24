"""

198. House Robber
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

PROBLEM:
You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money.
You cannot rob two adjacent houses, because that will alert the police.

Given an integer array nums, where nums[i] is the amount of money
in the i-th house, return the maximum amount of money you can rob
without robbing two adjacent houses.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: 4

Explanation:
Rob house 1 with money 1 and house 3 with money 3.
Total = 1 + 3 = 4.

Example 2:
Input: nums = [2, 7, 9, 3, 1]
Output: 12

Explanation:
Rob house 1 with money 2, house 3 with money 9,
and house 5 with money 1.
Total = 2 + 9 + 1 = 12.

APPROACH:
Use dynamic programming with two variables.

For every house, we have two choices:
1. Skip the current house.
2. Rob the current house and add its money to the best result
   from two houses before.

Formula:
current = max(previous_house, two_houses_before + nums[i])

We only need to store the previous two results, so we do not need
a full DP array.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        two_houses_before = 0
        previous_house = 0

        for money in nums:
            current = max(previous_house, two_houses_before + money)
            two_houses_before = previous_house
            previous_house = current

        return previous_house


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.rob([1, 2, 3, 1]))
    # 4

    print(solution.rob([2, 7, 9, 3, 1]))
    # 12

    print(solution.rob([1]))
    # 1

    print(solution.rob([2, 1, 1, 2]))
    # 4

    print(solution.rob([0]))
    # 0
