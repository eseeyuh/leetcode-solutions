"""

35. Search Insert Position
Difficulty: Easy
Link: https://leetcode.com/problems/search-insert-position/

PROBLEM:
Given a sorted array of distinct integers nums and a target value,
return the index if the target is found.

If the target is not found, return the index where it would be inserted
in order.

APPROACH:
This solution uses a linear scan.

We go through the array from left to right.
If nums[i] is equal to target, we return i.
If target is greater than nums[i], we update position to i + 1.

At the end, position will contain the place where target should be inserted.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        position = 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target > nums[i]:
                position = i + 1

        return position


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.searchInsert([1, 3, 5, 6], 5))
    # 2

    print(solution.searchInsert([1, 3, 5, 6], 2))
    # 1

    print(solution.searchInsert([1, 3, 5, 6], 7))
    # 4

    print(solution.searchInsert([1, 3, 5, 6], 0))
    # 0
