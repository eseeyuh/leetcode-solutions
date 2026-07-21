"""

29. Divide Two Integers
Difficulty: Medium
Link: https://leetcode.com/problems/divide-two-integers/

PROBLEM:
Given two integers dividend and divisor, divide them without using:
- multiplication
- division
- modulo operator

The integer division should truncate toward zero.

Return the quotient after dividing dividend by divisor.

If the quotient goes outside the 32-bit signed integer range:
[-2^31, 2^31 - 1]

clamp it to that range.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Explanation:
10 / 3 = 3.333...
After truncating toward zero, the result is 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Explanation:
7 / -3 = -2.333...
After truncating toward zero, the result is -2.

APPROACH:
Use subtraction with bit shifting.

Instead of subtracting divisor one by one, we repeatedly double the divisor
using left shift.

For example:
10 / 3

We can subtract:
3, 6, 12...

12 is too large, so we subtract 6.
That gives quotient part 2.

Then continue with the remaining value.

Bit shifting:
x << 1 means x doubled.

This avoids using multiplication, division, and modulo.

Time Complexity: O(log^2 n)
Space Complexity: O(1)

"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative_result = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            current_divisor = divisor
            current_quotient = 1

            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                current_quotient <<= 1

            dividend -= current_divisor
            quotient += current_quotient

        if negative_result:
            quotient = -quotient

        return quotient


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.divide(10, 3))
    # 3

    print(solution.divide(7, -3))
    # -2

    print(solution.divide(0, 1))
    # 0

    print(solution.divide(1, 1))
    # 1

    print(solution.divide(-2147483648, -1))
    # 2147483647

    print(solution.divide(-2147483648, 1))
    # -2147483648
