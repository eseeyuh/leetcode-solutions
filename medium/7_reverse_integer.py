"""

7. Reverse Integer
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-integer/

PROBLEM:
Given a signed 32-bit integer x, return x with its digits reversed.

If reversing x causes the value to go outside the signed 32-bit integer range:
[-2^31, 2^31 - 1]

then return 0.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

APPROACH:
Reverse the integer digit by digit.

At each step:
1. Take the last digit from x.
2. Remove the last digit from x.
3. Before adding the digit to the result, check if the result would overflow.
4. Add the digit to the reversed number.

We use truncation toward zero for negative numbers.

Time Complexity: O(log10(x))
Space Complexity: O(1)

"""

import math


class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        result = 0

        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > 7
            ):
                return 0

            if result < int(INT_MIN / 10) or (
                result == int(INT_MIN / 10) and digit < -8
            ):
                return 0

            result = result * 10 + digit

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.reverse(123))
    # 321

    print(solution.reverse(-123))
    # -321

    print(solution.reverse(120))
    # 21

    print(solution.reverse(0))
    # 0

    print(solution.reverse(1534236469))
    # 0

    print(solution.reverse(-2147483648))
    # 0
