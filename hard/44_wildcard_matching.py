"""

44. Wildcard Matching
Difficulty: Hard
Link: https://leetcode.com/problems/wildcard-matching/

PROBLEM:
Given an input string s and a pattern p, implement wildcard pattern matching
with support for '?' and '*'.

Rules:
- '?' matches any single character.
- '*' matches any sequence of characters, including the empty sequence.

The matching should cover the entire input string, not just part of it.

Example 1:
Input: s = "aa", p = "a"
Output: False

Explanation:
"a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: True

Explanation:
"*" matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: False

Explanation:
"?" matches "c", but "a" does not match "b".

APPROACH:
Use two pointers with greedy backtracking.

We keep:
- s_index: current position in s
- p_index: current position in p
- star_index: last position of "*" in p
- match_index: position in s where the last "*" started matching

While scanning:
1. If characters match, or p[p_index] is "?":
   move both pointers.

2. If p[p_index] is "*":
   remember this star position.
   Let "*" initially match an empty sequence.
   Move only p_index.

3. If characters do not match, but we have seen a "*":
   backtrack to the character after the last "*".
   Make "*" match one more character from s.
   Move s_index accordingly.

4. If characters do not match and there is no previous "*":
   return False.

After processing all characters in s, the remaining pattern must contain
only "*" characters.

Time Complexity: O(m + n)
Space Complexity: O(1)

where:
m = len(s)
n = len(p)

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s_index = 0
        p_index = 0

        star_index = -1
        match_index = 0

        while s_index < len(s):
            if (
                p_index < len(p)
                and (p[p_index] == s[s_index] or p[p_index] == "?")
            ):
                s_index += 1
                p_index += 1

            elif p_index < len(p) and p[p_index] == "*":
                star_index = p_index
                match_index = s_index
                p_index += 1

            elif star_index != -1:
                p_index = star_index + 1
                match_index += 1
                s_index = match_index

            else:
                return False

        while p_index < len(p) and p[p_index] == "*":
            p_index += 1

        return p_index == len(p)


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.isMatch("aa", "a"))
    # False

    print(solution.isMatch("aa", "*"))
    # True

    print(solution.isMatch("cb", "?a"))
    # False

    print(solution.isMatch("adceb", "*a*b"))
    # True

    print(solution.isMatch("acdcb", "a*c?b"))
    # False

    print(solution.isMatch("", "*"))
    # True

    print(solution.isMatch("", "?"))
    # False
