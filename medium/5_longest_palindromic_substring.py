"""

5. Longest Palindromic Substring
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/

PROBLEM:
Given a string s, return the longest palindromic substring in s.

A palindrome is a string that reads the same forward and backward.

Example:
Input: s = "babad"
Output: "bab"

Explanation:
"aba" is also a valid answer.

APPROACH:
Use the expand around center technique.

Every palindrome has a center.

There are two possible types of centers:
1. Odd length palindrome: one center character
   Example: "aba", center is "b"

2. Even length palindrome: two center characters
   Example: "bb", center is between two "b" characters

For each index, we check both cases:
- expand from i, i
- expand from i, i + 1

During expansion, while the left and right characters are equal,
we keep expanding outward.

Time Complexity: O(n^2)
Space Complexity: O(1)

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        result_start = 0
        result_length = 0

        def expand_from_center(left: int, right: int) -> None:
            nonlocal result_start, result_length

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > result_length:
                    result_start = left
                    result_length = current_length

                left -= 1
                right += 1

        for i in range(len(s)):
            expand_from_center(i, i)
            expand_from_center(i, i + 1)

        return s[result_start:result_start + result_length]


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.longestPalindrome("babad"))
    # "bab" or "aba"

    print(solution.longestPalindrome("cbbd"))
    # "bb"

    print(solution.longestPalindrome("a"))
    # "a"

    print(solution.longestPalindrome("ac"))
    # "a" or "c"

    print(solution.longestPalindrome("racecar"))
    # "racecar"
