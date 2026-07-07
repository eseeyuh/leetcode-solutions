"""

136. Single Number
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/

PROBLEM:
Given a non-empty array of integers nums, every element appears twice
except for one element.

Find the element that appears only once.

You must implement a solution with:
1. Linear runtime complexity.
2. Constant extra space.

Example 1:
Input: nums = [2, 2, 1]
Output: 1

Example 2:
Input: nums = [4, 1, 2, 1, 2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

APPROACH:
Use XOR.

XOR has useful properties:
1. a ^ a = 0
2. a ^ 0 = a
3. XOR order does not matter

Since every number appears twice except one,
all duplicate numbers cancel each other out.

The only number left after XOR-ing all elements is the single number.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result ^= num

        return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.singleNumber([2, 2, 1]))
    # 1

    print(solution.singleNumber([4, 1, 2, 1, 2]))
    # 4

    print(solution.singleNumber([1]))
    # 1

    print(solution.singleNumber([-1, -1, -2]))
    # -2

    print(solution.singleNumber([7, 3, 7]))
    # 3
