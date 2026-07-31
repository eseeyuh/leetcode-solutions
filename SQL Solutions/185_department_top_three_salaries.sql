/*
185. Department Top Three Salaries
Difficulty: Hard
Link: https://leetcode.com/problems/department-top-three-salaries/

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
Each row contains the ID and name of a department.

A high earner in a department is an employee who has a salary in the top three
unique salaries for that department.

Write a solution to find the employees who are high earners in each department.

Return the result table in any order.

Example:
Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
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
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

APPROACH:
Use DENSE_RANK.

We need the top three unique salaries inside each department.

PARTITION BY departmentId means:
create a separate ranking for each department.

ORDER BY salary DESC means:
the highest salary gets rank 1.

DENSE_RANK is important because equal salaries should have the same rank.
For example, in the IT department:
90000 -> rank 1
85000 -> rank 2
85000 -> rank 2
70000 -> rank 3
69000 -> rank 4

Then we keep only employees with salary_rank <= 3.

Finally, we join with Department to get the department name.

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
WHERE ranked_employees.salary_rank <= 3;
