"""

40. Combination Sum II
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-ii/

PROBLEM:
Given a collection of candidate numbers candidates and a target number target,
find all unique combinations in candidates where the candidate numbers sum
to target.

Each number in candidates may only be used once in the combination.

The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output:
[
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]

Example 2:
Input: candidates = [2, 5, 2, 1, 2], target = 5
Output:
[
    [1, 2, 2],
    [5]
]

APPROACH:
Use backtracking.

The key difference from Combination Sum I:
each number can be used only once.

So after choosing candidates[i], the next recursive call starts from i + 1.

To avoid duplicate combinations:
1. Sort candidates first.
2. When looping through candidates, skip duplicate values at the same recursion level.

For example:
if candidates[i] == candidates[i - 1] and i > start_index,
we skip candidates[i].

This prevents generating the same combination more than once.

If remaining becomes 0, we found a valid combination.
If remaining becomes negative, we stop exploring that path.

Time Complexity: O(2^n)
Space Complexity: O(n)

where:
n = length of candidates

"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def backtrack(start_index: int, current_combination: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(current_combination.copy())
                return

            if remaining < 0:
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                current_combination.append(candidates[i])

                backtrack(i + 1, current_combination, remaining - candidates[i])

                current_combination.pop()

        backtrack(0, [], target)

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
    # [[1, 2, 2], [5]]

    print(solution.combinationSum2([1, 1, 1, 1], 2))
    # [[1, 1]]

    print(solution.combinationSum2([1, 2], 4))
    # []

    print(solution.combinationSum2([3, 1, 3, 5, 1, 1], 8))
    # [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
