"""

28. Find the Index of the First Occurrence in a String
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

PROBLEM:
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack.

If needle is not part of haystack, return -1.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Explanation:
"sad" occurs at index 0 and index 6.
The first occurrence is at index 0.

APPROACH:
Use the KMP algorithm.

KMP avoids checking the same characters again and again.
First, we build the LPS array for needle.

LPS means Longest Prefix Suffix.
It tells us how far we can move back in needle when there is a mismatch.

Then we scan haystack and needle together.
If characters match, move both pointers.
If the full needle is matched, return the starting index.
If there is a mismatch, use the LPS array to avoid unnecessary comparisons.

Time Complexity: O(n + m)
Space Complexity: O(m)

where:
n = len(haystack)
m = len(needle)

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lps = [0] * len(needle)

        prev_lps = 0
        i = 1

        while i < len(needle):
            if needle[i] == needle[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        haystack_index = 0
        needle_index = 0

        while haystack_index < len(haystack):
            if haystack[haystack_index] == needle[needle_index]:
                haystack_index += 1
                needle_index += 1
            else:
                if needle_index == 0:
                    haystack_index += 1
                else:
                    needle_index = lps[needle_index - 1]

            if needle_index == len(needle):
                return haystack_index - len(needle)

        return -1


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.strStr("sadbutsad", "sad"))
    # 0

    print(solution.strStr("leetcode", "leeto"))
    # -1

    print(solution.strStr("hello", "ll"))
    # 2

    print(solution.strStr("aaaaa", "bba"))
    # -1

    print(solution.strStr("mississippi", "issip"))
    # 4
