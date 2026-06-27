"""

10. Regular Expression Matching
Difficulty: Hard
Link: https://leetcode.com/problems/regular-expression-matching/

PROBLEM:
Given an input string s and a pattern p, implement regular expression
matching with support for '.' and '*'.

Rules:
'.' matches any single character.
'*' matches zero or more of the preceding element.

Return True if the pattern matches the entire string.
Return False otherwise.

Example 1:
Input: s = "aa", p = "a"
Output: False

Explanation:
"a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: True

Explanation:
"a*" means zero or more of the preceding character 'a',
so it can match "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: True

Explanation:
".*" means zero or more of any character.

APPROACH:
Use dynamic programming with memoization.

We define a helper function:
dp(i, j)

It returns True if:
s[i:] matches p[j:]

At every position, we check if the current characters match:
- s[i] == p[j]
- or p[j] == '.'

Then we handle two cases:

1. If the next pattern character is '*':
   - skip the pattern part like "a*" completely
   - or use "*" to match the current character and move in s

2. Otherwise:
   - current characters must match
   - then move both i and j forward

Time Complexity: O(m * n)
Space Complexity: O(m * n)

where:
m = len(s)
n = len(p)

"""

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def dp(i: int, j: int) -> bool:

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                return dp(i, j + 2) or (first_match and dp(i + 1, j))

            return first_match and dp(i + 1, j + 1)

        return dp(0, 0)


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.isMatch("aa", "a"))
    # False

    print(solution.isMatch("aa", "a*"))
    # True

    print(solution.isMatch("ab", ".*"))
    # True

    print(solution.isMatch("aab", "c*a*b"))
    # True

    print(solution.isMatch("mississippi", "mis*is*p*."))
    # False

    print(solution.isMatch("ab", ".*c"))
    # False
