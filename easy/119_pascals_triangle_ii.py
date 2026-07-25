"""

119. Pascal's Triangle II
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle-ii/

PROBLEM:
Given an integer rowIndex, return the rowIndex-th row of Pascal's Triangle.

The rowIndex is 0-indexed.

In Pascal's Triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: rowIndex = 3
Output: [1, 3, 3, 1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1, 1]

APPROACH:
Build the row iteratively.

Start with the first row:
[1]

For every next row:
1. Add 1 at the end.
2. Update the middle values from right to left.
3. Each value becomes the sum of itself and the value before it.

We update from right to left so that we do not overwrite values that are still
needed for the calculation.

Time Complexity: O(rowIndex^2)
Space Complexity: O(rowIndex)

"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1]

        for _ in range(rowIndex):
            row.append(1)

            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.getRow(3))
    # [1, 3, 3, 1]

    print(solution.getRow(0))
    # [1]

    print(solution.getRow(1))
    # [1, 1]

    print(solution.getRow(4))
    # [1, 4, 6, 4, 1]

    print(solution.getRow(5))
    # [1, 5, 10, 10, 5, 1]
