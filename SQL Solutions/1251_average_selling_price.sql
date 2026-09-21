/*
1251. Average Selling Price
Difficulty: Easy
Link: https://leetcode.com/problems/average-selling-price/

PROBLEM:
Table: Prices

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+

(product_id, start_date, end_date) is the primary key for this table.
Each row indicates the price of a product in the period from start_date to end_date.
For each product_id, there will be no overlapping periods.

Table: UnitsSold

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+

This table may contain duplicate rows.
Each row indicates the date, units, and product_id of each product sold.

Write a solution to find the average selling price for each product.

average_price should be rounded to 2 decimal places.

If a product does not have any sold units, its average selling price is 0.

Return the result table in any order.

Example:
Input:
Prices table:
+------------+------------+------------+--------+
| product_id | start_date | end_date   | price  |
+------------+------------+------------+--------+
| 1          | 2019-02-17 | 2019-02-28 | 5      |
| 1          | 2019-03-01 | 2019-03-22 | 20     |
| 2          | 2019-02-01 | 2019-02-20 | 15     |
| 2          | 2019-02-21 | 2019-03-31 | 30     |
+------------+------------+------------+--------+

UnitsSold table:
+------------+---------------+-------+
| product_id | purchase_date | units |
+------------+---------------+-------+
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |
+------------+---------------+-------+

Output:
+------------+---------------+
| product_id | average_price |
+------------+---------------+
| 1          | 6.96          |
| 2          | 16.96         |
+------------+---------------+

APPROACH:
Use LEFT JOIN.

The Prices table tells us which price was active during each date range.
The UnitsSold table tells us how many units were sold on each purchase date.

We join the tables by:
1. product_id
2. purchase_date being between start_date and end_date

Then calculate the weighted average:

SUM(price * units) / SUM(units)

We use LEFT JOIN because products with no sold units should still appear
in the result with average_price = 0.

Time Complexity: O(n)
Space Complexity: O(result size)

*/

SELECT
    prices.product_id,

    CASE
        WHEN SUM(unitssold.units) IS NULL THEN 0
        ELSE ROUND(
            SUM(prices.price * unitssold.units) / SUM(unitssold.units),
            2
        )
    END AS average_price

FROM Prices AS prices

LEFT JOIN UnitsSold AS unitssold
    ON prices.product_id = unitssold.product_id
    AND unitssold.purchase_date BETWEEN prices.start_date AND prices.end_date

GROUP BY prices.product_id;
