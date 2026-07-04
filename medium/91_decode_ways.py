"""

91. Decode Ways
Difficulty: Medium
Link: https://leetcode.com/problems/decode-ways/

PROBLEM:
You have a secret message encoded as a string of numbers.

The decoding mapping is:
"1"  -> "A"
"2"  -> "B"
...
"25" -> "Y"
"26" -> "Z"

Given a string s containing only digits, return the number of ways
to decode it.

If the string cannot be decoded in any valid way, return 0.

Example 1:
Input: s = "12"
Output: 2

Explanation:
"12" can be decoded as:
1. "AB" -> 1, 2
2. "L"  -> 12

Example 2:
Input: s = "226"
Output: 3

Explanation:
"226" can be decoded as:
1. "BZ"  -> 2, 26
2. "VF"  -> 22, 6
3. "BBF" -> 2, 2, 6

Example 3:
Input: s = "06"
Output: 0

Explanation:
"06" is invalid because codes cannot start with 0.

APPROACH:
Use dynamic programming.

For every position, we check:
1. Can the current single digit be decoded?
   Valid single digits are "1" to "9".

2. Can the previous two digits be decoded together?
   Valid two-digit numbers are "10" to "26".

Formula:
current = ways using one digit + ways using two digits

We only need the previous two DP values, so we do not need a full DP array.

Time Complexity: O(n)
Space Complexity: O(1)

"""


class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        two_steps_before = 1
        one_step_before = 1

        for i in range(1, len(s)):
            current = 0

            if s[i] != "0":
                current += one_step_before

            two_digit_number = int(s[i - 1:i + 1])

            if 10 <= two_digit_number <= 26:
                current += two_steps_before

            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.numDecodings("12"))
    # 2

    print(solution.numDecodings("226"))
    # 3

    print(solution.numDecodings("06"))
    # 0

    print(solution.numDecodings("11106"))
    # 2

    print(solution.numDecodings("10"))
    # 1

    print(solution.numDecodings("27"))
    # 1
