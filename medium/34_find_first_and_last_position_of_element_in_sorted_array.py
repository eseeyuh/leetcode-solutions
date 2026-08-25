"""

34. Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

PROBLEM:
Given an array of integers nums sorted in non-decreasing order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example 2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]

Example 3:
Input: nums = [], target = 0
Output: [-1, -1]

APPROACH:
Use binary search twice.

Since the array is sorted, we can find:
1. The first position of target.
2. The last position of target.

For the first position:
- If nums[mid] is greater than or equal to target, move right to mid - 1.
- Otherwise, move left to mid + 1.
- When nums[mid] equals target, save mid as a possible answer.

For the last position:
- If nums[mid] is less than or equal to target, move left to mid + 1.
- Otherwise, move right to mid - 1.
- When nums[mid] equals target, save mid as a possible answer.

Time Complexity: O(log n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_position = self.find_first_position(nums, target)
        last_position = self.find_last_position(nums, target)

        return [first_position, last_position]

    def find_first_position(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    result = mid

                right = mid - 1
            else:
                left = mid + 1

        return result

    def find_last_position(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    result = mid

                left = mid + 1
            else:
                right = mid - 1

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    # [3, 4]

    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
    # [-1, -1]

    print(solution.searchRange([], 0))
    # [-1, -1]

    print(solution.searchRange([1], 1))
    # [0, 0]

    print(solution.searchRange([2, 2, 2, 2], 2))
    # [0, 3]
