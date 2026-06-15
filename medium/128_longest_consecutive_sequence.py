"""

128. Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

PROBLEM:
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4

Explanation:
The longest consecutive sequence is [1, 2, 3, 4], so the answer is 4.

APPROACH:
Use a set for O(1) average lookup.

For each number, only start counting if it is the beginning of a sequence.
A number is the beginning of a sequence if num - 1 is not in the set.

Then count forward:
num, num + 1, num + 2, ...

This ensures each sequence is counted only once.

Time Complexity: O(n)
Space Complexity: O(n)

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                current_length = 1

                while current + 1 in num_set:
                    current += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
    # 4

    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    # 9

    print(solution.longestConsecutive([]))
    # 0

    print(solution.longestConsecutive([1]))
    # 1

    print(solution.longestConsecutive([1, 2, 2, 3]))
    # 3
