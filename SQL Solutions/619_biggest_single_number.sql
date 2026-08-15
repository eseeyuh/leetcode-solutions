/*
619. Biggest Single Number
Difficulty: Easy
Link: https://leetcode.com/problems/biggest-single-number/

PROBLEM:
Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+

This table may contain duplicates.
There is no primary key for this table.

Each row contains an integer.

A single number is a number that appears only once in the MyNumbers table.

Find the largest single number.

If there is no single number, report NULL.

Example 1:
Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+

Output:
+-----+
| num |
+-----+
| 6   |
+-----+

Explanation:
The single numbers are 1, 4, 5, and 6.
The largest one is 6.

Example 2:
Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+

Output:
+------+
| num  |
+------+
| NULL |
+------+

Explanation:
There are no single numbers, so we return NULL.

APPROACH:
Use GROUP BY and HAVING.

First, group rows by num.
Then keep only numbers that appear exactly once using:

HAVING COUNT(*) = 1

After that, use MAX(num) to find the largest single number.

If there are no single numbers, MAX returns NULL automatically.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    MAX(num) AS num
FROM (
    SELECT
        num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
