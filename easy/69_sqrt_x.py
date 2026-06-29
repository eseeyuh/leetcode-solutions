"""

69. Sqrt(x)
Difficulty: Easy
Link: https://leetcode.com/problems/sqrtx/

PROBLEM:
Given a non-negative integer x, return the square root of x rounded down
to the nearest integer.

The returned integer should be the largest integer r such that:

r * r <= x

You must not use any built-in exponent function or operator.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2

Explanation:
The square root of 8 is 2.828...
Rounded down, the answer is 2.

APPROACH:
Use binary search.

The answer is somewhere between 0 and x.

For a middle number mid:
- if mid * mid == x, then mid is the exact square root
- if mid * mid < x, mid may be the answer, but we try bigger numbers
- if mid * mid > x, mid is too large, so we try smaller numbers

We keep track of the best valid answer seen so far.

Time Complexity: O(log x)
Space Complexity: O(1)

"""


class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left = 1
        right = x // 2
        answer = 1

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid

            if square < x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.mySqrt(4))
    # 2

    print(solution.mySqrt(8))
    # 2

    print(solution.mySqrt(0))
    # 0

    print(solution.mySqrt(1))
    # 1

    print(solution.mySqrt(2147395599))
    # 46339
