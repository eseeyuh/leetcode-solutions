"""

48. Rotate Image
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/

PROBLEM:
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees clockwise.

You have to rotate the image in-place, which means you must modify
the input matrix directly.

Do not allocate another 2D matrix.

Example 1:
Input:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

Example 2:
Input:
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

Output:
[
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]

APPROACH:
Rotate the matrix in two steps:

1. Transpose the matrix.
   This means swapping matrix[i][j] with matrix[j][i].

   Example:
   [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]

   becomes:

   [
       [1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]
   ]

2. Reverse each row.

   [
       [1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]
   ]

   becomes:

   [
       [7, 4, 1],
       [8, 5, 2],
       [9, 6, 3]
   ]

This gives a 90-degree clockwise rotation.

Time Complexity: O(n^2)
Space Complexity: O(1)

The matrix is modified in-place.

"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution.rotate(matrix)
    print(matrix)
    # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    solution.rotate(matrix)
    print(matrix)
    # [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    matrix = [[1]]

    solution.rotate(matrix)
    print(matrix)
    # [[1]]
