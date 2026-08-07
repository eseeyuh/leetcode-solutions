/*
577. Employee Bonus
Difficulty: Easy
Link: https://leetcode.com/problems/employee-bonus/

PROBLEM:
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+

empId is the column with unique values for this table.

Each row contains:
- employee id
- employee name
- supervisor id
- employee salary

Table: Bonus

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+

empId is the column with unique values for this table.
empId is a foreign key referencing Employee.empId.

Each row contains the id of an employee and their bonus.

Write a solution to report the name and bonus amount of each employee who satisfies
either of the following:

1. The employee has a bonus less than 1000.
2. The employee did not get any bonus.

Return the result table in any order.

Example:
Input:
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | NULL       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+

Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+

Output:
+------+-------+
| name | bonus |
+------+-------+
| Brad | NULL  |
| John | NULL  |
| Dan  | 500   |
+------+-------+

APPROACH:
Use LEFT JOIN.

We need to include employees even if they do not have a row in Bonus.
That is why LEFT JOIN is used.

After joining:
- If the employee has no bonus, b.bonus will be NULL.
- If the employee has a bonus less than 1000, we include them.

So the condition is:
b.bonus < 1000 OR b.bonus IS NULL

Time Complexity: O(n + m), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    e.name,
    b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
    ON e.empId = b.empId
WHERE b.bonus < 1000
   OR b.bonus IS NULL;
