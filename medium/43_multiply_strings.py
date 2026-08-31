"""

43. Multiply Strings
Difficulty: Medium
Link: https://leetcode.com/problems/multiply-strings/

PROBLEM:
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

You must not use any built-in BigInteger library or convert the inputs
to integers directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

APPROACH:
Simulate multiplication by hand.

If num1 has length m and num2 has length n,
the result can have at most m + n digits.

For every pair of digits:
- multiply num1[i] and num2[j]
- place the result into the correct positions in the result array

The digit from num1[i] and num2[j] contributes to:
- position i + j + 1 for the current digit
- position i + j for the carry

For example:
num1 = "123"
num2 = "456"

We multiply every digit pair and accumulate the result in an array.

After all multiplications, we remove leading zeros and convert the array
back into a string.

Time Complexity: O(m * n)
Space Complexity: O(m + n)

where:
m = len(num1)
n = len(num2)

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                multiplication = digit1 * digit2

                position_for_digit = i + j + 1
                position_for_carry = i + j

                total = multiplication + result[position_for_digit]

                result[position_for_digit] = total % 10
                result[position_for_carry] += total // 10

        while result[0] == 0:
            result.pop(0)

        return "".join(str(digit) for digit in result)


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.multiply("2", "3"))
    # "6"

    print(solution.multiply("123", "456"))
    # "56088"

    print(solution.multiply("0", "456"))
    # "0"

    print(solution.multiply("999", "999"))
    # "998001"

    print(solution.multiply("12", "34"))
    # "408"
