"""

76. Minimum Window Substring
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/

PROBLEM:
Given two strings s and t, return the minimum window substring of s
such that every character in t, including duplicates, is included
in the window.

If there is no such substring, return an empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Explanation:
The minimum window substring "BANC" includes 'A', 'B', and 'C'.

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""

APPROACH:
Use sliding window with character counts.

First, count how many times each character is needed from t.

Then move the right pointer through s and add characters into the window.

When the window contains all required characters with correct frequencies,
try to shrink it from the left side to make it smaller.

We keep track of the smallest valid window found.

Time Complexity: O(m + n)
Space Complexity: O(m + n)

where:
m = len(s)
n = len(t)

"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0
        best_length = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    # "BANC"

    print(solution.minWindow("a", "a"))
    # "a"

    print(solution.minWindow("a", "aa"))
    # ""

    print(solution.minWindow("aa", "aa"))
    # "aa"

    print(solution.minWindow("ab", "b"))
    # "b"
