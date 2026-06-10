"""
27. Remove Element
Difficulty: Easy
Link: https://leetcode.com/problems/remove-element/

PROBLEM:
Given an integer array nums and an integer val, remove all
occurrences of val in nums in-place. The order of the elements
may be changed.

Return the number of elements in nums which are not equal to val.
The first k elements of nums should contain the elements that are
not equal to val. The remaining elements are not important.

APPROACH:
Use a pointer k to track the position where the next valid element
should be placed. Iterate through nums. If the current element is
not equal to val, write it to nums[k] and increase k.

"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 2, 2, 3]
    k1 = solution.removeElement(nums1, 3)
    print(k1, nums1[:k1])  # 2 [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = solution.removeElement(nums2, 2)
    print(k2, nums2[:k2])  # 5 [0, 1, 3, 0, 4]

    nums3 = []
    k3 = solution.removeElement(nums3, 1)
    print(k3, nums3[:k3])  # 0 []
