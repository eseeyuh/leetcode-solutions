"""

16. 3Sum Closest
Difficulty: Medium
Link: https://leetcode.com/problems/3sum-closest/

PROBLEM:
Given an integer array nums and an integer target, find three integers
at distinct indices such that their sum is closest to target.

Return the sum of the three integers.

You may assume that each input has exactly one solution.

Example 1:
Input: nums = [-1, 2, 1, -4], target = 1
Output: 2

Explanation:
The sum closest to target is 2:
-1 + 2 + 1 = 2

Example 2:
Input: nums = [0, 0, 0], target = 1
Output: 0

APPROACH:
Sort the array first.

Then fix one number nums[i].
For the remaining part of the array, use two pointers:
left = i + 1
right = len(nums) - 1

Calculate the current sum:
nums[i] + nums[left] + nums[right]

If this sum is closer to target than the best sum so far,
update the best sum.

If the current sum is smaller than target, move left to the right
to increase the sum.

If the current sum is greater than target, move right to the left
to decrease the sum.

If the current sum is exactly equal to target, return target immediately
because we cannot get closer than exact match.

Time Complexity: O(n^2)
Space Complexity: O(1), excluding the sorting space used by Python

"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target

        return closest_sum


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    # 2

    print(solution.threeSumClosest([0, 0, 0], 1))
    # 0

    print(solution.threeSumClosest([1, 1, 1, 0], -100))
    # 2

    print(solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
    # -2
