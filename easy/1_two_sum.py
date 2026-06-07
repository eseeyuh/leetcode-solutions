"""
==================================================
1. Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
==================================================

PROBLEM:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up
to target. Each input has exactly one solution, and you
may not use the same element twice.

APPROACH:
Use a hash map to store each number and its index as we
iterate. For each number, calculate the complement
(target - num) and check if it already exists in the map.
If it does, we found our pair. Otherwise, store the
current number and continue.

Time complexity:   3 ms
Space complexity:  20.59 MB
==================================================
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))        # [1, 2]
    print(solution.twoSum([3, 3], 6))            # [0, 1]
