"""

33. Search in Rotated Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

PROBLEM:
There is an integer array nums sorted in ascending order with distinct values.

Before being passed to the function, nums may be rotated at an unknown index.

Example:
Original array:
[0, 1, 2, 4, 5, 6, 7]

After rotation:
[4, 5, 6, 7, 0, 1, 2]

Given the rotated array nums and an integer target, return the index of target.
If target is not in nums, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

APPROACH:
Use binary search.

Even though the whole array is rotated, at least one half is always sorted.

At every step:
1. Find the middle element.
2. If nums[mid] is the target, return mid.
3. Check which half is sorted.
4. Decide whether the target is inside the sorted half.
5. Move left or right accordingly.

This keeps the search O(log n).

Time Complexity: O(log n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    # 4

    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
    # -1

    print(solution.search([1], 0))
    # -1

    print(solution.search([1], 1))
    # 0

    print(solution.search([3, 1], 1))
    # 1
