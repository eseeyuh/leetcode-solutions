"""

36. Valid Sudoku
Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

PROBLEM:
Determine if a 9 x 9 Sudoku board is valid.

Only the filled cells need to be validated according to these rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition.

Notes:
- A partially filled Sudoku board can be valid but not necessarily solvable.
- Only filled cells need to be validated.
- Empty cells are represented by ".".

Example 1:
Input:
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: True

Example 2:
Input:
Same as Example 1, but the top-left "5" is changed to "8".
Output: False

Explanation:
There are two 8's in the top-left 3 x 3 sub-box.

APPROACH:
Use sets to track seen digits.

We need to make sure there are no repeated digits in:
1. rows
2. columns
3. 3 x 3 boxes

For every filled cell board[row][col]:
- Check if the digit already exists in the current row.
- Check if the digit already exists in the current column.
- Check if the digit already exists in the current 3 x 3 box.

The box index can be represented as:
(row // 3, col // 3)

If the digit already exists in any of these places, the board is invalid.

Otherwise, add the digit to the corresponding row, column, and box sets.

Time Complexity: O(1)

The board is always 9 x 9, so the number of cells is fixed.
If generalized to an n x n board, the complexity would be O(n^2).

Space Complexity: O(1)

The maximum number of stored digits is limited by the fixed 9 x 9 board size.

"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                box_key = (row // 3, col // 3)

                if (
                    value in rows[row]
                    or value in columns[col]
                    or value in boxes[box_key]
                ):
                    return False

                rows[row].add(value)
                columns[col].add(value)
                boxes[box_key].add(value)

        return True


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.isValidSudoku(board))
    # True

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.isValidSudoku(board))
    # False

    board = [["."] * 9 for _ in range(9)]
    print(solution.isValidSudoku(board))
    # True
