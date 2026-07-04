"""

115. Distinct Subsequences
Difficulty: Hard
Link: https://leetcode.com/problems/distinct-subsequences/

PROBLEM:
Given two strings s and t, return the number of distinct subsequences
of s which equal t.

A subsequence is made by deleting some characters from a string without
changing the order of the remaining characters.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5

APPROACH:
Use dynamic programming.

dp[j] means:
the number of ways to form t[:j] using the characters of s processed so far.

Base case:
dp[0] = 1

Why?
There is exactly one way to form an empty string:
choose nothing.

For every character in s, we move through t backwards.
If s character equals t[j - 1], then this character can be used
to form t[:j].

So:
dp[j] += dp[j - 1]

We go backwards to avoid using the same character of s more than once.

Time Complexity: O(m * n)
Space Complexity: O(n)

where:
m = len(s)
n = len(t)

"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(t) > len(s):
            return 0

        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(len(t), 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[len(t)]


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.numDistinct("rabbbit", "rabbit"))
    # 3

    print(solution.numDistinct("babgbag", "bag"))
    # 5

    print(solution.numDistinct("abc", "abc"))
    # 1

    print(solution.numDistinct("abc", "ac"))
    # 1

    print(solution.numDistinct("abc", "abcd"))
    # 0
