"""

15. 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

PROBLEM:
Given an integer array nums, return all unique triplets
[nums[i], nums[j], nums[k]] such that:

i != j
i != k
j != k
nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

APPROACH:
Sort the array first.

Then fix one number nums[i].
For the remaining part of the array, use two pointers:
left = i + 1
right = len(nums) - 1

We need:
nums[i] + nums[left] + nums[right] == 0

If the sum is too small, move left to the right.
If the sum is too large, move right to the left.
If the sum is zero, save the triplet and skip duplicates.

Time Complexity: O(n^2)
Space Complexity: O(1), excluding the output array

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    # [[-1, -1, 2], [-1, 0, 1]]

    print(solution.threeSum([0, 1, 1]))
    # []

    print(solution.threeSum([0, 0, 0]))
    # [[0, 0, 0]]

    print(solution.threeSum([0, 0, 0, 0]))
    # [[0, 0, 0]]

    print(solution.threeSum([-2, 0, 1, 1, 2]))
    # [[-2, 0, 2], [-2, 1, 1]]
