/*
184. Department Highest Salary
Difficulty: Medium
Link: https://leetcode.com/problems/department-highest-salary/

PROBLEM:
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+

id is the primary key for this table.
departmentId is a foreign key referencing Department.id.

Each row contains:
- employee id
- employee name
- employee salary
- employee department id

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

id is the primary key for this table.
department name is guaranteed to be not NULL.

Write a solution to find employees who have the highest salary in each department.

Return the result table in any order.

Example:
Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+

APPROACH:
Use DENSE_RANK.

We rank employees inside each department by salary in descending order.

PARTITION BY departmentId means:
start a separate ranking for each department.

ORDER BY salary DESC means:
highest salary gets rank 1.

DENSE_RANK is useful because if two employees have the same highest salary,
both get rank 1 and both should be returned.

Then join with Department to get the department name.

Time Complexity: O(n log n), because of ranking/sorting
Space Complexity: O(n), depending on the database engine

*/

SELECT
    d.name AS Department,
    ranked_employees.name AS Employee,
    ranked_employees.salary AS Salary
FROM (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
) AS ranked_employees
JOIN Department AS d
    ON ranked_employees.departmentId = d.id
WHERE ranked_employees.salary_rank = 1;
