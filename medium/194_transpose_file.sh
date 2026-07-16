#!/bin/bash

# 194. Transpose File
# Difficulty: Medium
# Link: https://leetcode.com/problems/transpose-file/
#
# PROBLEM:
# Given a text file file.txt, transpose its content.
#
# Each row has the same number of columns.
# Each field is separated by a space.
#
# Example:
# Input file.txt:
# name age
# alice 21
# ryan 30
#
# Output:
# name alice ryan
# age 21 30
#
# APPROACH:
# Use awk.
#
# awk reads the file line by line.
# NF is the number of fields in the current row.
#
# For every field:
# - NR is the current row number.
# - i is the current column number.
# - matrix[i, NR] stores the value from row NR and column i.
#
# After reading the whole file, we print values column by column.
# This creates the transposed output.
#
# Time Complexity: O(rows * columns)
# Space Complexity: O(rows * columns)

awk '
{
    for (i = 1; i <= NF; i++) {
        matrix[i, NR] = $i
    }
}

{
    if (NF > columns) {
        columns = NF
    }
}

END {
    for (i = 1; i <= columns; i++) {
        line = matrix[i, 1]

        for (j = 2; j <= NR; j++) {
            line = line " " matrix[i, j]
        }

        print line
    }
}
' file.txt
