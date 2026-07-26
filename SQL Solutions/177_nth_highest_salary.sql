/*
177. Nth Highest Salary
Difficulty: Medium
Link: https://leetcode.com/problems/nth-highest-salary/

PROBLEM:
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+

id is the primary key for this table.
Each row contains information about the salary of an employee.

Write a solution to find the nth highest distinct salary from the Employee table.

If there are less than n distinct salaries, return NULL.

Example 1:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

n = 2

Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Example 2:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

n = 2

Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| NULL                   |
+------------------------+

APPROACH:
Use DENSE_RANK.

We need the nth highest distinct salary.

DENSE_RANK gives the same rank to equal salaries.
For example:
300 -> rank 1
200 -> rank 2
200 -> rank 2
100 -> rank 3

Then we return the salary where rank = N.

If there is no such rank, the query returns NULL.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(n), depending on the database engine

*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT salary
        FROM (
            SELECT
                salary,
                DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
            FROM Employee
            GROUP BY salary
        ) AS ranked_salaries
        WHERE salary_rank = N
    );
END;
