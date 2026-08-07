/*
584. Find Customer Referee
Difficulty: Easy
Link: https://leetcode.com/problems/find-customer-referee/

PROBLEM:
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+

id is the primary key for this table.

Each row contains:
- customer id
- customer name
- id of the customer who referred them

Find the names of customers who are either:

1. referred by any customer with id != 2
2. not referred by any customer

Return the result table in any order.

Example:
Input:
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | NULL       |
| 2  | Jane | NULL       |
| 3  | Alex | 2          |
| 4  | Bill | NULL       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+

Output:
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

APPROACH:
Use WHERE with two conditions.

We need customers whose referee_id is not 2.
But we also need customers with no referee.

In SQL, NULL cannot be compared with != directly.
So we must handle NULL separately using IS NULL.

The condition becomes:
referee_id != 2 OR referee_id IS NULL

Time Complexity: O(n)
Space Complexity: O(result size)

*/

SELECT
    name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;
