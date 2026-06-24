"""

70. Climbing Stairs
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

PROBLEM:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can climb either 1 or 2 steps.

Return the number of distinct ways you can climb to the top.

Example 1:
Input: n = 2
Output: 2

Explanation:
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3

Explanation:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

APPROACH:
This is a dynamic programming problem.

To reach step n, you can come from:
1. step n - 1 by taking 1 step
2. step n - 2 by taking 2 steps

So:
ways(n) = ways(n - 1) + ways(n - 2)

This is the same pattern as Fibonacci numbers.

We only need to keep the previous two results:
one_step_before = ways(i - 1)
two_steps_before = ways(i - 2)

Time Complexity: O(n)
Space Complexity: O(1)

"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        two_steps_before = 1
        one_step_before = 2

        for step in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.climbStairs(1))
    # 1

    print(solution.climbStairs(2))
    # 2

    print(solution.climbStairs(3))
    # 3

    print(solution.climbStairs(4))
    # 5

    print(solution.climbStairs(5))
    # 8
