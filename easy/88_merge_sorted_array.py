"""

88. Merge Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/merge-sorted-array/

PROBLEM:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order.

You are also given two integers:
m = number of valid elements in nums1
n = number of valid elements in nums2

nums1 has length m + n.
The first m elements are real values.
The last n elements are zeros and should be ignored.

Merge nums2 into nums1 as one sorted array.

The final sorted array should be stored inside nums1.
The function should not return anything.

Example 1:
Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
Output: [1, 2, 2, 3, 5, 6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

APPROACH:
Use three pointers and merge from the end.

p1 points to the last valid element in nums1.
p2 points to the last element in nums2.
insert_pos points to the last available position in nums1.

We compare nums1[p1] and nums2[p2].
The bigger value goes to nums1[insert_pos].

This works because nums1 has empty space at the end.
By filling from the end, we do not overwrite useful values in nums1.

Time Complexity: O(m + n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m - 1
        p2 = n - 1
        insert_pos = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[insert_pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[insert_pos] = nums2[p2]
                p2 -= 1

            insert_pos -= 1


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
    # [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    print(nums1)
    # [1]

    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    print(nums1)
    # [1]

    nums1 = [2, 0]
    solution.merge(nums1, 1, [1], 1)
    print(nums1)
    # [1, 2]
