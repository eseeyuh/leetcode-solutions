"""
==================================================
217. Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/
==================================================

PROBLEM:
Given an integer array nums, return True if any value
appears at least twice, and False if every element is distinct.

APPROACH:
Use a set to track numbers we have already seen.
If the current number is already in the set, we found a duplicate.
Otherwise, add it to the set and continue.

==================================================
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))  # True
    print(solution.containsDuplicate([1, 2, 3, 4]))  # False
    print(solution.containsDuplicate([1, 1, 1, 3]))  # True
