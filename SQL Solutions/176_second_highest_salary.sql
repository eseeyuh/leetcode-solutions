/*
176. Second Highest Salary
Difficulty: Medium
Link: https://leetcode.com/problems/second-highest-salary/

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

Write a solution to find the second highest distinct salary from the Employee table.

If there is no second highest salary, return NULL.

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

Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| NULL                |
+---------------------+

APPROACH:
Use a subquery.

First, select distinct salaries.
Then sort them in descending order.
The highest salary is at offset 0.
The second highest salary is at offset 1.

If there is no second highest salary, the subquery returns NULL.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(n), depending on the database engine

*/

SELECT
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary;
