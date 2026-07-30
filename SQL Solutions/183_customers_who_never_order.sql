/*
183. Customers Who Never Order
Difficulty: Easy
Link: https://leetcode.com/problems/customers-who-never-order/

PROBLEM:
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

id is the primary key for this table.
Each row contains the ID and name of a customer.

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+

id is the primary key for this table.
customerId is a foreign key referencing Customers.id.

Each row contains the ID of an order and the ID of the customer who ordered it.

Write a solution to find all customers who never order anything.

Return the result table in any order.

Example:
Input:
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

APPROACH:
Use LEFT JOIN.

We need all customers from the Customers table.
Then we join Orders by customer ID.

If a customer has no orders, the matching Orders columns will be NULL.

So we keep only rows where Orders.customerId IS NULL.

Time Complexity: O(n + m), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    c.name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o
    ON c.id = o.customerId
WHERE o.customerId IS NULL;
