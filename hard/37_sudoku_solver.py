"""

37. Sudoku Solver
Difficulty: Hard
Link: https://leetcode.com/problems/sudoku-solver/

PROBLEM:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A Sudoku solution must satisfy all of the following rules:

1. Each digit 1-9 must occur exactly once in each row.
2. Each digit 1-9 must occur exactly once in each column.
3. Each digit 1-9 must occur exactly once in each of the nine 3 x 3 sub-boxes.

The "." character indicates an empty cell.

It is guaranteed that the input board has only one solution.

The board must be modified in-place.
Do not return anything.

Example:
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

Output:
board = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

APPROACH:
Use backtracking.

First, collect:
1. digits already used in each row
2. digits already used in each column
3. digits already used in each 3 x 3 box
4. positions of all empty cells

Then try to fill empty cells one by one.

For each empty cell:
- Try digits from "1" to "9".
- A digit is valid if it is not already used in the same row, column, or box.
- If valid, place it and continue solving the next empty cell.
- If the next steps fail, remove the digit and try another one.

This is classic backtracking:
choose -> explore -> undo

Since the problem guarantees one valid solution, once we fill all empty cells,
the board is solved.

Time Complexity: O(9^m)
Space Complexity: O(m)

where:
m = number of empty cells

In practice, using sets for rows, columns, and boxes makes validation fast.

"""

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == ".":
                    empty_cells.append((row, col))
                else:
                    rows[row].add(value)
                    columns[col].add(value)
                    boxes[self.get_box_index(row, col)].add(value)

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            row, col = empty_cells[index]
            box_index = self.get_box_index(row, col)

            for digit in "123456789":
                if (
                    digit in rows[row]
                    or digit in columns[col]
                    or digit in boxes[box_index]
                ):
                    continue

                board[row][col] = digit
                rows[row].add(digit)
                columns[col].add(digit)
                boxes[box_index].add(digit)

                if backtrack(index + 1):
                    return True

                board[row][col] = "."
                rows[row].remove(digit)
                columns[col].remove(digit)
                boxes[box_index].remove(digit)

            return False

        backtrack(0)

    def get_box_index(self, row: int, col: int) -> int:
        return (row // 3) * 3 + (col // 3)


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

    solution.solveSudoku(board)

    for row in board:
        print(row)

    # Expected:
    # ["5","3","4","6","7","8","9","1","2"]
    # ["6","7","2","1","9","5","3","4","8"]
    # ["1","9","8","3","4","2","5","6","7"]
    # ["8","5","9","7","6","1","4","2","3"]
    # ["4","2","6","8","5","3","7","9","1"]
    # ["7","1","3","9","2","4","8","5","6"]
    # ["9","6","1","5","3","7","2","8","4"]
    # ["2","8","7","4","1","9","6","3","5"]
    # ["3","4","5","2","8","6","1","7","9"]
