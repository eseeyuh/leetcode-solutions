"""
==================================================
125. Valid Palindrome
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/
==================================================

PROBLEM:
A phrase is a palindrome if, after converting all uppercase
letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and
backward. Given a string s, return true if it is a
palindrome, or false otherwise.

APPROACH:
Use two pointers, one starting from the left and one from
the right. Skip any non-alphanumeric characters on both
sides. Compare the characters (case-insensitively) at each
pointer. If they ever differ, it's not a palindrome.
Otherwise move both pointers inward until they meet.

Time complexity:   O(n)
Space complexity:  O(1)
==================================================
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(solution.isPalindrome("race a car"))                       # False
    print(solution.isPalindrome(" "))                                # True
