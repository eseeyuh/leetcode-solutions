/*
197. Rising Temperature
Difficulty: Easy
Link: https://leetcode.com/problems/rising-temperature/

PROBLEM:
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+

id is the column with unique values for this table.
There are no different rows with the same recordDate.

This table contains information about the temperature on a certain day.

Write a solution to find all dates' id with higher temperatures compared to
the previous date, meaning yesterday.

Return the result table in any order.

Example:
Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+

Explanation:
On 2015-01-02, the temperature was higher than the previous day:
10 -> 25

On 2015-01-04, the temperature was higher than the previous day:
20 -> 30

APPROACH:
Use a self join.

We compare the Weather table with itself:

- today represents the current date.
- yesterday represents the previous date.

We join rows where the difference between the dates is exactly 1 day.

Then we keep only rows where:
today.temperature > yesterday.temperature

Time Complexity: O(n^2), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    today.id
FROM Weather AS today
JOIN Weather AS yesterday
    ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;
