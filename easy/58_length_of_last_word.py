"""

58. Length of Last Word
Difficulty: Easy
Link: https://leetcode.com/problems/length-of-last-word/

PROBLEM:
Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example:
Input: s = "Hello World"
Output: 5

Explanation:
The last word is "World", and its length is 5.

APPROACH:
Start from the end of the string.

First, skip all trailing spaces.
Then count characters until we reach another space or the beginning
of the string.

This avoids creating an extra list of words.

Time Complexity: O(n)
Space Complexity: O(1)

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        index = len(s) - 1
        length = 0

        while index >= 0 and s[index] == " ":
            index -= 1

        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1

        return length


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLastWord("Hello World"))
    # 5

    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    # 4

    print(solution.lengthOfLastWord("luffy is still joyboy"))
    # 6

    print(solution.lengthOfLastWord("a"))
    # 1

    print(solution.lengthOfLastWord("day"))
    # 3
