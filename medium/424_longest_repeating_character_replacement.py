"""

424. Longest Repeating Character Replacement
Difficulty: Medium
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

PROBLEM:
You are given a string s and an integer k.

You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing at most k replacements.

Example:
Input: s = "ABAB", k = 2
Output: 4

Explanation:
Replace the two 'A's with two 'B's or the two 'B's with two 'A's.

APPROACH:
Use a sliding window.

The window represents the current substring we are trying to make
into one repeating character.

For every window:
window length - frequency of the most common character = replacements needed

If replacements needed is greater than k, the window is invalid,
so we move the left pointer to shrink it.

Time Complexity: O(n)
Space Complexity: O(1), because there are only 26 uppercase English letters

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.characterReplacement("ABAB", 2))
    # 4

    print(solution.characterReplacement("AABABBA", 1))
    # 4

    print(solution.characterReplacement("AAAA", 2))
    # 4

    print(solution.characterReplacement("ABCDE", 1))
    # 2

    print(solution.characterReplacement("BAAA", 0))
    # 3
