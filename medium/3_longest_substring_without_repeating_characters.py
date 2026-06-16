"""

3. Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

PROBLEM:
Given a string s, find the length of the longest substring
without duplicate characters.

A substring must be continuous.

Example:
Input: s = "abcabcbb"
Output: 3

Explanation:
The answer is "abc", with length 3.

APPROACH:
Use a sliding window.

The window represents the current substring without duplicate characters.

We use a dictionary to store the last index where each character appeared.

If we meet a repeated character inside the current window,
we move the left border of the window after the previous occurrence
of that character.

At each step, we update the maximum window length.

Time Complexity: O(n)
Space Complexity: O(min(n, m))
where m is the size of the character set.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLongestSubstring("abcabcbb"))
    # 3

    print(solution.lengthOfLongestSubstring("bbbbb"))
    # 1

    print(solution.lengthOfLongestSubstring("pwwkew"))
    # 3

    print(solution.lengthOfLongestSubstring(""))
    # 0

    print(solution.lengthOfLongestSubstring(" "))
    # 1

    print(solution.lengthOfLongestSubstring("dvdf"))
    # 3
