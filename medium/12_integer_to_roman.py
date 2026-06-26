"""

12. Integer to Roman
Difficulty: Medium
Link: https://leetcode.com/problems/integer-to-roman/

PROBLEM:
Seven different symbols represent Roman numerals:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Given an integer num, convert it to a Roman numeral.

Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"

Explanation:
3000 = MMM
700 = DCC
40 = XL
9 = IX

Example 2:
Input: num = 58
Output: "LVIII"

Example 3:
Input: num = 1994
Output: "MCMXCIV"

APPROACH:
Use greedy conversion.

Create a list of Roman numeral values from largest to smallest.
For each value:
1. While num is greater than or equal to that value,
   append the corresponding Roman symbol to the result.
2. Subtract the value from num.

This works because Roman numerals are built from largest values to smallest,
including special subtractive forms like:
900 = CM
400 = CD
90 = XC
40 = XL
9 = IX
4 = IV

Time Complexity: O(1)
Space Complexity: O(1)

The constraints are fixed: 1 <= num <= 3999.
So the number of Roman symbols and operations is bounded.

"""


class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        result = []

        for i in range(len(values)):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]

        return "".join(result)


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.intToRoman(3749))
    # "MMMDCCXLIX"

    print(solution.intToRoman(58))
    # "LVIII"

    print(solution.intToRoman(1994))
    # "MCMXCIV"

    print(solution.intToRoman(4))
    # "IV"

    print(solution.intToRoman(3999))
    # "MMMCMXCIX"
