/*
570. Managers with at Least 5 Direct Reports
Difficulty: Medium
Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

PROBLEM:
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+

id is the primary key for this table.

Each row contains:
- employee id
- employee name
- department
- managerId, which is the id of their manager

If managerId is NULL, the employee does not have a manager.
No employee will be the manager of themself.

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

Example:
Input:
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | NULL      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+

Output:
+------+
| name |
+------+
| John |
+------+

APPROACH:
Use GROUP BY and HAVING.

First, group employees by managerId.
Each group represents the direct reports of one manager.

Then keep only managerId values where the number of direct reports is at least 5.

After that, join this result back to Employee to get the manager's name.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    e.name
FROM Employee AS e
JOIN (
    SELECT
        managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) AS managers
    ON e.id = managers.managerId;
