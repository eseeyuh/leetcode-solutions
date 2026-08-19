/*
627. Swap Salary
Difficulty: Easy
Link: https://leetcode.com/problems/swap-salary/

PROBLEM:
Table: Salary

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+

id is the primary key for this table.

The sex column is an ENUM with values:
- 'm'
- 'f'

Write a solution to swap all 'f' and 'm' values:
- change all 'f' values to 'm'
- change all 'm' values to 'f'

Important:
You must write a single UPDATE statement.
Do not use SELECT.
Do not use intermediate temporary tables.

Example:
Input:
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+

Output:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+

APPROACH:
Use UPDATE with CASE.

CASE checks the current value of sex:
- if sex = 'm', set it to 'f'
- otherwise, set it to 'm'

This swaps all values in one update statement.

Time Complexity: O(n)
Space Complexity: O(1)

*/

UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
END;
