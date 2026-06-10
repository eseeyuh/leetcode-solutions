"""

238. Product of Array Except Self
Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

PROBLEM:
Given an integer array nums, return an array answer where answer[i]
is equal to the product of all elements of nums except nums[i].

You must solve it in O(n) time and without using division.

FOLLOW-UP:
Solve it in O(1) extra space.
The output array does not count as extra space.

APPROACH:
For each index i, the answer is:

product of all numbers to the left of i
*
product of all numbers to the right of i

We first store prefix products in the answer array.
Then we move from right to left and multiply each position by the suffix product.

This avoids division and uses only the output array plus two variables.

Time Complexity: O(n)
Space Complexity: O(1), excluding the output array

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.productExceptSelf([1, 2, 3, 4]))
    # [24, 12, 8, 6]

    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
    # [0, 0, 9, 0, 0]

    print(solution.productExceptSelf([1, 2]))
    # [2, 1]

    print(solution.productExceptSelf([0, 0]))
    # [0, 0]
