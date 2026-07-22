"""

45. Jump Game II
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game-ii/

PROBLEM:
You are given a 0-indexed array of integers nums.

You are initially positioned at index 0.

Each nums[i] represents the maximum length of a forward jump from index i.

If you are at index i, you can jump to any index i + j where:
0 <= j <= nums[i]
i + j < n

Return the minimum number of jumps needed to reach the last index.

The test cases guarantee that the last index is reachable.

Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: 2

Explanation:
Jump from index 0 to index 1.
Then jump from index 1 to the last index.

Example 2:
Input: nums = [2, 3, 0, 1, 4]
Output: 2

APPROACH:
Use a greedy approach.

We keep track of:
1. jumps - how many jumps we have made.
2. current_end - the farthest index we can reach using the current number of jumps.
3. farthest - the farthest index we can reach using one more jump.

We iterate through the array except the last index.

For every index, we update farthest:
farthest = max(farthest, i + nums[i])

When we reach current_end, it means we have used all positions available
with the current jump count. So we must make another jump and update
current_end to farthest.

This gives the minimum number of jumps because we always choose the jump
range that allows us to reach as far as possible.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.jump([2, 3, 1, 1, 4]))
    # 2

    print(solution.jump([2, 3, 0, 1, 4]))
    # 2

    print(solution.jump([0]))
    # 0

    print(solution.jump([1, 2, 3]))
    # 2

    print(solution.jump([1, 1, 1, 1]))
    # 3
