"""

31. Next Permutation
Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/

PROBLEM:
A permutation of an array of integers is an arrangement of its members.

The next permutation is the next lexicographically greater arrangement.
If there is no greater arrangement, rearrange the array into the lowest
possible order, which means ascending order.

The replacement must be done in-place and use only constant extra memory.

Example 1:
Input: nums = [1, 2, 3]
Output: [1, 3, 2]

Example 2:
Input: nums = [3, 2, 1]
Output: [1, 2, 3]

Example 3:
Input: nums = [1, 1, 5]
Output: [1, 5, 1]

APPROACH:
Use the standard next permutation algorithm.

Steps:
1. Find the first index i from the right where nums[i] < nums[i + 1].
   This is the place where we can make the number bigger.

2. If such index exists, find the first index j from the right where
   nums[j] > nums[i].

3. Swap nums[i] and nums[j].

4. Reverse the part after index i.
   This makes the suffix as small as possible.

If no such i exists, the array is in descending order.
That means it is already the largest permutation, so we reverse the whole array.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)
    # [1, 3, 2]

    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    print(nums)
    # [1, 2, 3]

    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    print(nums)
    # [1, 5, 1]

    nums = [1, 3, 2]
    solution.nextPermutation(nums)
    print(nums)
    # [2, 1, 3]

    nums = [2, 3, 1]
    solution.nextPermutation(nums)
    print(nums)
    # [3, 1, 2]
