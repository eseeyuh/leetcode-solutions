/*
181. Employees Earning More Than Their Managers
Difficulty: Easy
Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/

PROBLEM:
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+

id is the primary key for this table.

Each row contains:
- employee id
- employee name
- employee salary
- managerId, which points to another employee's id

Write a solution to find employees who earn more than their managers.

Return the result table in any order.

Example:
Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+

Explanation:
Joe earns 70000.
Joe's manager is Sam, who earns 60000.
Since 70000 > 60000, Joe is included.

APPROACH:
Use a self join.

The Employee table contains both employees and managers.
So we join Employee with itself:

- e represents the employee
- m represents the manager

Then we compare:
e.salary > m.salary

If the employee earns more than the manager, return the employee name.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    e.name AS Employee
FROM Employee AS e
JOIN Employee AS m
    ON e.managerId = m.id
WHERE e.salary > m.salary;
