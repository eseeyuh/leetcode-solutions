"""

118. Pascal's Triangle
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle/

PROBLEM:
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle:
1. The first and last numbers of every row are 1.
2. Every middle number is the sum of the two numbers directly above it.

Example 1:
Input: numRows = 5
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Example 2:
Input: numRows = 1
Output: [[1]]

APPROACH:
Build the triangle row by row.

For each row:
1. Create a row filled with 1s.
2. For every middle position, calculate the value as:
   previous_row[j - 1] + previous_row[j]
3. Add the completed row to the triangle.

Time Complexity: O(numRows^2)
Space Complexity: O(numRows^2)

The output itself contains numRows^2 elements in total.

"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for row_index in range(numRows):
            row = [1] * (row_index + 1)

            for column in range(1, row_index):
                row[column] = (
                    triangle[row_index - 1][column - 1]
                    + triangle[row_index - 1][column]
                )

            triangle.append(row)

        return triangle


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.generate(5))
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    print(solution.generate(1))
    # [[1]]

    print(solution.generate(2))
    # [[1], [1, 1]]

    print(solution.generate(3))
    # [[1], [1, 1], [1, 2, 1]]
