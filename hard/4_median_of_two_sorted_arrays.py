"""

4. Median of Two Sorted Arrays
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

PROBLEM:
Given two sorted arrays nums1 and nums2 of size m and n,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(m + n)).

Example 1:
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.00000

Example 2:
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.50000

APPROACH:
Use binary search on the smaller array.

We split both arrays into left and right parts so that:
1. The left part contains half of all elements.
2. Every element in the left part is <= every element in the right part.

If the partition is correct:
- If total length is odd, the median is the maximum element on the left side.
- If total length is even, the median is the average of:
  max left element and min right element.

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total_length = m + n
        half_length = (total_length + 1) // 2

        left = 0
        right = m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half_length - partition1

            max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float("inf") if partition1 == m else nums1[partition1]

            max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float("inf") if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total_length % 2 == 1:
                    return float(max(max_left1, max_left2))

                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2

            elif max_left1 > min_right2:
                right = partition1 - 1

            else:
                left = partition1 + 1

        return 0.0


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.findMedianSortedArrays([1, 3], [2]))
    # 2.0

    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    # 2.5

    print(solution.findMedianSortedArrays([], [1]))
    # 1.0

    print(solution.findMedianSortedArrays([2], []))
    # 2.0

    print(solution.findMedianSortedArrays([0, 0], [0, 0]))
    # 0.0
