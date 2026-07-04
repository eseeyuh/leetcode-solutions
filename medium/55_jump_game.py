"""

55. Jump Game
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game/

PROBLEM:
You are given an integer array nums.

You start at index 0, and each element represents the maximum jump length
from that position.

Return True if you can reach the last index, otherwise return False.

Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: True

Example 2:
Input: nums = [3, 2, 1, 0, 4]
Output: False

APPROACH:
Use a greedy algorithm.

Keep track of the farthest index we can currently reach.

For every index:
1. If the current index is beyond the farthest reachable index,
   we cannot continue, so return False.
2. Update the farthest reachable index.
3. If the farthest reachable index reaches the last position,
   return True.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest = 0

        for index, jump in enumerate(nums):
            if index > farthest:
                return False

            farthest = max(farthest, index + jump)

            if farthest >= len(nums) - 1:
                return True

        return True


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.canJump([2, 3, 1, 1, 4]))
    # True

    print(solution.canJump([3, 2, 1, 0, 4]))
    # False

    print(solution.canJump([0]))
    # True

    print(solution.canJump([2, 0, 0]))
    # True

    print(solution.canJump([1, 0, 1]))
    # False
