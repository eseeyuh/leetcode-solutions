"""
==================================================
49. Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
==================================================

PROBLEM:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An anagram is a word formed by rearranging the letters of
another word using all original letters exactly once.

APPROACH:
Sort each word alphabetically to produce a key — all anagrams
share the same sorted key. Use a defaultdict to map each key
to a list of words. Append every word to its group, then
return all groups as a list.

Time complexity:   7 ms
Space complexity:  22.15 MB
==================================================
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagram_map[key].append(word)
        return list(anagram_map.values())


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    print(solution.groupAnagrams([""]))   # [[""]]
    print(solution.groupAnagrams(["a"]))  # [["a"]]
