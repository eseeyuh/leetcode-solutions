/*
180. Consecutive Numbers
Difficulty: Medium
Link: https://leetcode.com/problems/consecutive-numbers/

PROBLEM:
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+

id is the primary key for this table.
id is an autoincrement column starting from 1.

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

Example:
Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

Explanation:
1 is the only number that appears consecutively at least three times.

APPROACH:
Use a self join.

We join the Logs table with itself three times:

- l1 is the first row
- l2 is the next row
- l3 is the row after that

Then we check:
l1.id + 1 = l2.id
l1.id + 2 = l3.id

and all three nums are equal.

Use DISTINCT because the same number can appear in more than one group
of three consecutive rows.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(result size)

*/

SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM Logs AS l1
JOIN Logs AS l2
    ON l1.id + 1 = l2.id
JOIN Logs AS l3
    ON l1.id + 2 = l3.id
WHERE l1.num = l2.num
  AND l2.num = l3.num;
