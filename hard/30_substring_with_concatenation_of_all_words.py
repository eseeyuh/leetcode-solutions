"""

30. Substring with Concatenation of All Words
Difficulty: Hard
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

PROBLEM:
You are given a string s and an array of strings words.

All strings in words have the same length.

A concatenated string is a string that contains all the strings from words
exactly once, in any order, concatenated together.

Return all starting indices of substrings in s that are concatenated strings.

The answer can be returned in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo", "bar"]
Output: [0, 9]

Explanation:
The substring starting at 0 is "barfoo".
The substring starting at 9 is "foobar".

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]
Output: [6, 9, 12]

APPROACH:
Use a sliding window.

All words have the same length, so we can move through s in chunks of word_len.

For every possible offset from 0 to word_len - 1:
1. Move through the string word by word.
2. Keep a window of words and their counts.
3. If a word is valid, add it to the current window.
4. If a word appears too many times, shrink the window from the left.
5. If the window contains exactly all words, save the left index.
6. If a word is not in words, reset the window.

We use Counter to store the required frequency of each word.

Time Complexity: O(n * word_len)
Space Complexity: O(words.length)

More commonly, since word_len is limited and we scan each character offset,
this is considered O(n) relative to the length of s.

"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []

        required_counts = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            current_counts = defaultdict(int)
            words_in_window = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in required_counts:
                    current_counts[word] += 1
                    words_in_window += 1

                    while current_counts[word] > required_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        words_in_window -= 1
                        left += word_len

                    if words_in_window == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        words_in_window -= 1
                        left += word_len

                else:
                    current_counts.clear()
                    words_in_window = 0
                    left = right + word_len

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    # [0, 9]

    print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    # []

    print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    # [6, 9, 12]

    print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    # [8]

    print(solution.findSubstring("aaaaaa", ["aa", "aa"]))
    # [0, 1, 2]
