"""

42. Trapping Rain Water
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water/

PROBLEM:
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6

Explanation:
The elevation map can trap 6 units of rain water.

Example 2:
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9

APPROACH:
Use two pointers.

Water above a bar depends on the smaller wall between:
1. the highest wall on the left
2. the highest wall on the right

For each position:
water = min(left_max, right_max) - height[i]

Instead of precomputing left_max and right_max arrays,
we use two pointers and keep:
- left_max
- right_max

If height[left] is smaller than height[right],
the amount of water at left depends on left_max,
because there is already a taller or equal wall on the right.

So:
- update left_max
- add left_max - height[left]
- move left

Otherwise:
- update right_max
- add right_max - height[right]
- move right

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]

                right -= 1

        return trapped_water


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # 6

    print(solution.trap([4, 2, 0, 3, 2, 5]))
    # 9

    print(solution.trap([1]))
    # 0

    print(solution.trap([1, 2, 3]))
    # 0

    print(solution.trap([3, 2, 1]))
    # 0

    print(solution.trap([2, 0, 2]))
    # 2
