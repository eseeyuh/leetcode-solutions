"""

22. Generate Parentheses
Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses/

PROBLEM:
Given n pairs of parentheses, generate all combinations of well-formed
parentheses.

Example 1:
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Example 2:
Input: n = 1
Output: ["()"]

APPROACH:
Use backtracking.

We build the current parentheses string step by step.

At every step, we can:
1. Add "(" if we still have opening parentheses available.
2. Add ")" if the number of closing parentheses used is less than
   the number of opening parentheses used.

This guarantees that we never create an invalid sequence.

When the current string has length 2 * n, we add it to the result.

Time Complexity: O(4^n / sqrt(n))
Space Complexity: O(n), excluding the output array

The number of valid combinations is the nth Catalan number.

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.generateParenthesis(1))
    # ["()"]

    print(solution.generateParenthesis(2))
    # ["(())", "()()"]

    print(solution.generateParenthesis(3))
    # ["((()))", "(()())", "(())()", "()(())", "()()()"]

    print(solution.generateParenthesis(4))
    # 14 combinations
