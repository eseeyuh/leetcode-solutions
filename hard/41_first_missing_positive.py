"""

41. First Missing Positive
Difficulty: Hard
Link: https://leetcode.com/problems/first-missing-positive/

PROBLEM:
Given an unsorted integer array nums, return the smallest positive integer
that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1)
auxiliary space.

Example 1:
Input: nums = [1, 2, 0]
Output: 3

Explanation:
The numbers in the range [1, 2] are all in the array.

Example 2:
Input: nums = [3, 4, -1, 1]
Output: 2

Explanation:
1 is in the array but 2 is missing.

Example 3:
Input: nums = [7, 8, 9, 11, 12]
Output: 1

Explanation:
The smallest positive integer 1 is missing.

APPROACH:
Use the input array itself as storage.

For an array of length n, the first missing positive must be in the range
1 to n + 1.

Why?
- If all numbers from 1 to n are present, the answer is n + 1.
- Otherwise, some number from 1 to n is missing.

So we try to place every valid number x at index x - 1.

For example:
- 1 should be at index 0
- 2 should be at index 1
- 3 should be at index 2

We repeatedly swap nums[i] into its correct position while:
1. nums[i] is in the range [1, n]
2. nums[i] is not already in its correct position

After this placement step, we scan the array:
- If nums[i] != i + 1, then i + 1 is the smallest missing positive.

If all positions are correct, return n + 1.

Time Complexity: O(n)
Space Complexity: O(1)

Each number is moved to its correct position at most once.

"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            while (
                1 <= nums[i] <= n
                and nums[nums[i] - 1] != nums[i]
            ):
                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.firstMissingPositive([1, 2, 0]))
    # 3

    print(solution.firstMissingPositive([3, 4, -1, 1]))
    # 2

    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
    # 1

    print(solution.firstMissingPositive([1]))
    # 2

    print(solution.firstMissingPositive([2, 1]))
    # 3

    print(solution.firstMissingPositive([1, 1]))
    # 2
