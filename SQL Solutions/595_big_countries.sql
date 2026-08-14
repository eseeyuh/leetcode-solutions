/*
595. Big Countries
Difficulty: Easy
Link: https://leetcode.com/problems/big-countries/

PROBLEM:
Table: World

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+

name is the primary key for this table.

Each row contains information about:
- country name
- continent
- area
- population
- GDP

A country is big if:
1. it has an area of at least 3,000,000 km²
OR
2. it has a population of at least 25,000,000

Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

Example:
Input:
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+

Output:
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

APPROACH:
Use WHERE with OR.

A country should be included if at least one of the two conditions is true:
- area >= 3000000
- population >= 25000000

Then select only the required columns:
name, population, area.

Time Complexity: O(n)
Space Complexity: O(result size)

*/

SELECT
    name,
    population,
    area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
