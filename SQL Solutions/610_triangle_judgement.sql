/*
610. Triangle Judgement
Difficulty: Easy
Link: https://leetcode.com/problems/triangle-judgement/

PROBLEM:
Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+

(x, y, z) is the primary key for this table.

Each row contains the lengths of three line segments.

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

Example:
Input:
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+

Output:
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

APPROACH:
Use the triangle inequality theorem.

Three sides can form a triangle only if all three conditions are true:
1. x + y > z
2. x + z > y
3. y + z > x

If all conditions are true, return "Yes".
Otherwise, return "No".

Time Complexity: O(n)
Space Complexity: O(result size)

*/

SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z
         AND x + z > y
         AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
