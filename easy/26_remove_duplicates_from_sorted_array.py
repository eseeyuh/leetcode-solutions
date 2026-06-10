"""
26. Remove Duplicates from Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

PROBLEM:
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should
be kept the same.

Return the number of unique elements in nums. The first k
elements of nums should contain the unique elements in the
same order. The remaining elements are not important.

APPROACH:
Use two pointers. The variable k represents the position
where the next unique element should be placed. Iterate
through nums starting from index 1. If the current element
is different from the last unique element, place it at nums[k]
and increase k.

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # 2 [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # 5 [0, 1, 2, 3, 4]

    nums3 = []
    k3 = solution.removeDuplicates(nums3)
    print(k3, nums3[:k3])  # 0 []
