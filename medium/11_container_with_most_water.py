"""

11. Container With Most Water
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

PROBLEM:
You are given an integer array height of length n.
There are n vertical lines where the i-th line has height height[i].

Choose two lines that, together with the x-axis, form a container.
Return the maximum amount of water the container can store.

The container cannot be slanted.

APPROACH:
Use two pointers.

Start with the widest possible container:
left pointer at the beginning and right pointer at the end.

Calculate the area:
width * min(height[left], height[right])

Then move the pointer with the smaller height, because the smaller wall
limits the water amount. Moving the taller wall cannot increase the height
of the container, while the width always becomes smaller.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # 49

    print(solution.maxArea([1, 1]))
    # 1

    print(solution.maxArea([4, 3, 2, 1, 4]))
    # 16

    print(solution.maxArea([1, 2, 1]))
    # 2
