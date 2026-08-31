"""

46. Permutations
Difficulty: Medium
Link: https://leetcode.com/problems/permutations/

PROBLEM:
Given an array nums of distinct integers, return all possible permutations.

The answer can be returned in any order.

Example 1:
Input: nums = [1, 2, 3]
Output:
[
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

Example 2:
Input: nums = [0, 1]
Output:
[
    [0, 1],
    [1, 0]
]

Example 3:
Input: nums = [1]
Output:
[
    [1]
]

APPROACH:
Use backtracking.

A permutation uses every number exactly once.

We build a current path:
- At each step, try every number from nums.
- If the number was already used, skip it.
- Otherwise, add it to the path and mark it as used.
- Continue recursively.
- After recursion, undo the choice by removing it from the path
  and marking it as unused.

When the path length equals len(nums), we have a complete permutation.
Add a copy of the path to the result.

Time Complexity: O(n * n!)
Space Complexity: O(n)

where:
n = len(nums)

There are n! permutations, and copying each permutation takes O(n).

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        current_permutation = []
        used = set()

        def backtrack() -> None:
            if len(current_permutation) == len(nums):
                result.append(current_permutation.copy())
                return

            for num in nums:
                if num in used:
                    continue

                current_permutation.append(num)
                used.add(num)

                backtrack()

                current_permutation.pop()
                used.remove(num)

        backtrack()

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.permute([1, 2, 3]))
    # [
    #     [1, 2, 3],
    #     [1, 3, 2],
    #     [2, 1, 3],
    #     [2, 3, 1],
    #     [3, 1, 2],
    #     [3, 2, 1]
    # ]

    print(solution.permute([0, 1]))
    # [[0, 1], [1, 0]]

    print(solution.permute([1]))
    # [[1]]
