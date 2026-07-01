"""

18. 4Sum
Difficulty: Medium
Link: https://leetcode.com/problems/4sum/

PROBLEM:
Given an integer array nums and an integer target, return all unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

a, b, c, and d are distinct
nums[a] + nums[b] + nums[c] + nums[d] == target

The answer must not contain duplicate quadruplets.

Example 1:
Input: nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

Example 2:
Input: nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]

APPROACH:
Sort the array first.

Then fix two numbers:
nums[i] and nums[j]

For the remaining part of the array, use two pointers:
left = j + 1
right = len(nums) - 1

Now we need:
nums[i] + nums[j] + nums[left] + nums[right] == target

If the sum is too small, move left to the right.
If the sum is too large, move right to the left.
If the sum equals target, save the quadruplet and skip duplicates.

Sorting helps us:
1. Use two pointers efficiently.
2. Avoid duplicate quadruplets.

Time Complexity: O(n^3)
Space Complexity: O(1), excluding the output array

"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
    # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    print(solution.fourSum([2, 2, 2, 2, 2], 8))
    # [[2, 2, 2, 2]]

    print(solution.fourSum([], 0))
    # []

    print(solution.fourSum([1, 2, 3], 6))
    # []

    print(solution.fourSum([-3, -1, 0, 2, 4, 5], 0))
    # [[-3, -1, 0, 4]]
