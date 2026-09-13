/*
1068. Product Sales Analysis I
Difficulty: Easy
Link: https://leetcode.com/problems/product-sales-analysis-i/

PROBLEM:
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+

Write a solution to report the product_name, year, and price
for each sale_id in the Sales table.

Return the resulting table in any order.

APPROACH:
Use LEFT JOIN.

The Sales table contains product_id, year, and price.
The Product table contains product_name.

We join Sales with Product using product_id.

LEFT JOIN keeps all rows from Sales.
For every matching product_id, it adds the product_name from Product.

Time Complexity: O(n)
Space Complexity: O(result size)

*/

SELECT
    products.product_name,
    sales.year,
    sales.price
FROM Sales AS sales
LEFT JOIN Product AS products
    ON sales.product_id = products.product_id;
