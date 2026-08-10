/*
586. Customer Placing the Largest Number of Orders
Difficulty: Easy
Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

PROBLEM:
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+

order_number is the primary key for this table.

This table contains:
- order_number: the order ID
- customer_number: the customer ID

Write a solution to find the customer_number for the customer who has placed
the largest number of orders.

The test cases are generated so that exactly one customer will have placed
more orders than any other customer.

Example:
Input:
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+

Output:
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+

Explanation:
Customer 3 has two orders.
Customers 1 and 2 have one order each.
So customer 3 placed the largest number of orders.

APPROACH:
Use GROUP BY and COUNT.

GROUP BY customer_number groups all orders by customer.
COUNT(*) counts how many orders each customer placed.

Then we sort by the order count in descending order and keep only the first row.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(result size)

*/

SELECT
    customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;


/*
FOLLOW-UP:
If more than one customer has the largest number of orders,
return all such customers.

This version uses DENSE_RANK.

Customers with the same number of orders get the same rank.
Then we return all customers with rank 1.
*/

/*
WITH ranked_customers AS (
    SELECT
        customer_number,
        DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS order_rank
    FROM Orders
    GROUP BY customer_number
)
SELECT
    customer_number
FROM ranked_customers
WHERE order_rank = 1;
*/
