/*
1075. Project Employees I
Difficulty: Easy
Link: https://leetcode.com/problems/project-employees-i/

PROBLEM:
Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+

(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to the Employee table.

Each row indicates that an employee is working on a project.

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+

employee_id is the primary key of this table.
experience_years is guaranteed to be not NULL.

Each row contains information about one employee.

Write an SQL query that reports the average experience years of all employees
for each project, rounded to 2 digits.

Return the result table in any order.

Example:
Input:
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

Output:
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+

APPROACH:
Use JOIN, GROUP BY, AVG, and ROUND.

First, join Project with Employee using employee_id.
This gives each project the experience_years of every employee working on it.

Then group rows by project_id.
For each project, calculate the average experience_years using AVG.

Finally, round the average to 2 decimal places using ROUND(..., 2).

Time Complexity: O(n + m), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project AS p
JOIN Employee AS e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;
