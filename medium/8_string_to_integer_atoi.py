"""

8. String to Integer (atoi)
Difficulty: Medium
Link: https://leetcode.com/problems/string-to-integer-atoi/

PROBLEM:
Implement the myAtoi(string s) function, which converts a string
to a 32-bit signed integer.

The algorithm:
1. Ignore leading whitespace.
2. Check if the next character is '-' or '+'.
3. Read digits until a non-digit character is found.
4. If no digits are read, return 0.
5. Clamp the result to the 32-bit signed integer range:
   [-2^31, 2^31 - 1]

Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = " -042"
Output: -42

Example 3:
Input: s = "1337c0d3"
Output: 1337

Example 4:
Input: s = "0-1"
Output: 0

Example 5:
Input: s = "words and 987"
Output: 0

APPROACH:
Use a pointer index to scan the string.

First, skip leading spaces.
Then check the optional sign.
Then read digits one by one and build the number.

While building the number, check if it goes outside the 32-bit range.
If it does, return INT_MAX or INT_MIN depending on the sign.

Time Complexity: O(n)
Space Complexity: O(1)

"""


class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        index = 0
        sign = 1
        result = 0
        n = len(s)

        while index < n and s[index] == " ":
            index += 1

        if index < n and s[index] in ["-", "+"]:
            if s[index] == "-":
                sign = -1
            index += 1

        while index < n and s[index].isdigit():
            digit = int(s[index])

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        return sign * result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.myAtoi("42"))
    # 42

    print(solution.myAtoi(" -042"))
    # -42

    print(solution.myAtoi("1337c0d3"))
    # 1337

    print(solution.myAtoi("0-1"))
    # 0

    print(solution.myAtoi("words and 987"))
    # 0

    print(solution.myAtoi("-91283472332"))
    # -2147483648

    print(solution.myAtoi("91283472332"))
    # 2147483647
