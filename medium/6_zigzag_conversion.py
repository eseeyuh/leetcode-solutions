"""

6. Zigzag Conversion
Difficulty: Medium
Link: https://leetcode.com/problems/zigzag-conversion/

PROBLEM:
The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows.

Example for numRows = 3:

P   A   H   N
A P L S I I G
Y   I   R

Then it is read line by line:
"PAHNAPLSIIGYIR"

Given a string s and an integer numRows, return the converted string.

APPROACH:
Use a list of strings, where each string represents one row.

We move through the input string character by character.
For each character:
1. Add it to the current row.
2. If we are at the first row, start moving down.
3. If we are at the last row, start moving up.
4. Move to the next row according to the current direction.

At the end, join all rows together.

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    print(solution.convert("PAYPALISHIRING", 3))
    # "PAHNAPLSIIGYIR"

    print(solution.convert("PAYPALISHIRING", 4))
    # "PINALSIGYAHRPI"

    print(solution.convert("A", 1))
    # "A"

    print(solution.convert("AB", 1))
    # "AB"

    print(solution.convert("ABC", 2))
    # "ACB"
