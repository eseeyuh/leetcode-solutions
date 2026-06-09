"""

3689. Maximum Total Subarray Value I
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-total-subarray-value-i/

PROBLEM:
You are given an integer array nums and an integer k.
You need to choose exactly k non-empty subarrays.
Subarrays may overlap, and the same subarray may be chosen more than once.

The value of a subarray is:
max(subarray) - min(subarray)

Return the maximum possible total value after choosing exactly k subarrays.

APPROACH:
Because the same subarray can be chosen multiple times, we only need to find
the maximum possible value of one subarray.

The best possible subarray value is:
max(nums) - min(nums)

Then we choose that best subarray k times, so the answer is:
(max(nums) - min(nums)) * k

"""

from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        smallest = min(nums)
        largest = max(nums)
        best_value = largest - smallest
        return best_value * k


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.maxTotalValue([1, 3, 2], 2))
    # 4

    print(solution.maxTotalValue([4, 2, 5, 1], 3))
    # 12

    print(solution.maxTotalValue([5], 10))
    # 0
