/*
626. Exchange Seats
Difficulty: Medium
Link: https://leetcode.com/problems/exchange-seats/

PROBLEM:
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+

id is the primary key for this table.
Each row contains:
- student id
- student name

The id sequence always starts from 1 and increments continuously.

Write a solution to swap the seat id of every two consecutive students.

If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

Example:
Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+

Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+

APPROACH:
Use CASE to calculate the new id.

For every pair:
- odd id moves to id + 1
- even id moves to id - 1

But if the last id is odd, it should stay the same.

So:
1. If id is odd and it is the last row, keep id.
2. If id is odd, change it to id + 1.
3. If id is even, change it to id - 1.

Finally, order the result by the new id.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(result size)

*/

SELECT
    CASE
        WHEN id % 2 = 1 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id;
