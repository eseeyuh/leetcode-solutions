"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters

Examples:
    s = "anagram", t = "nagaram" -> True
    s = "rat",     t = "car"     -> False

"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()

    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("ab", "ba") is True
    assert sol.isAnagram("ab", "a") is False
    assert sol.isAnagram("", "") is True

    print("All tests passed.")
