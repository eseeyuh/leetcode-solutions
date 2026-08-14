/*
607. Sales Person
Difficulty: Easy
Link: https://leetcode.com/problems/sales-person/

PROBLEM:
Table: SalesPerson

+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+

sales_id is the primary key for this table.

Each row contains:
- salesperson id
- salesperson name
- salary
- commission rate
- hire date

Table: Company

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+

com_id is the primary key for this table.

Each row contains:
- company id
- company name
- city

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+

order_id is the primary key for this table.
com_id references Company.com_id.
sales_id references SalesPerson.sales_id.

Each row contains information about one order.

Write a solution to find the names of all salespersons who did not have
any orders related to the company with the name "RED".

Return the result table in any order.

Example:
Input:
SalesPerson table:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+

Company table:
+--------+--------+----------+
| com_id | name   | city     |
+--------+--------+----------+
| 1      | RED    | Boston   |
| 2      | ORANGE | New York |
| 3      | YELLOW | Boston   |
| 4      | GREEN  | Austin   |
+--------+--------+----------+

Orders table:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+

Output:
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+

APPROACH:
Use NOT IN with a subquery.

First, find all sales_id values that have orders related to company "RED".
To do that:
1. Join Orders with Company.
2. Keep only rows where Company.name = "RED".
3. Select the sales_id values from those rows.

Then, from SalesPerson, return only salespersons whose sales_id is not in that list.

Time Complexity: O(n + m), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT
        o.sales_id
    FROM Orders AS o
    JOIN Company AS c
        ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
