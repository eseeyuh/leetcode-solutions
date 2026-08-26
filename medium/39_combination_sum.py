"""

39. Combination Sum
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum/

PROBLEM:
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one chosen number
is different.

The answer can be returned in any order.

Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Explanation:
2 + 2 + 3 = 7
7 = 7

Example 2:
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

APPROACH:
Use backtracking.

We build combinations step by step.

At each step, we decide which candidate to add next.
Because the same number can be reused unlimited times, after choosing
candidates[i], we call backtrack again with the same index i.

To avoid duplicate combinations, we only move forward in the candidates array.
That means:
- [2, 2, 3] can be created
- but [3, 2, 2] will not be created separately

If the remaining target becomes 0, we found a valid combination.

If the remaining target becomes negative, we stop exploring that path.

Time Complexity: O(2^target)
Space Complexity: O(target)

The exact complexity depends on the values in candidates and the number
of valid combinations.

"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start_index: int, current_combination: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(current_combination.copy())
                return

            if remaining < 0:
                return

            for i in range(start_index, len(candidates)):
                current_combination.append(candidates[i])

                backtrack(i, current_combination, remaining - candidates[i])

                current_combination.pop()

        backtrack(0, [], target)

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.combinationSum([2, 3, 6, 7], 7))
    # [[2, 2, 3], [7]]

    print(solution.combinationSum([2, 3, 5], 8))
    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    print(solution.combinationSum([2], 1))
    # []

    print(solution.combinationSum([1], 1))
    # [[1]]

    print(solution.combinationSum([1], 2))
    # [[1, 1]]
