/*
585. Investments in 2016
Difficulty: Medium
Link: https://leetcode.com/problems/investments-in-2016/

PROBLEM:
Table: Insurance

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+

pid is the primary key for this table.

Each row contains information about one policy:
- pid is the policyholder's policy ID
- tiv_2015 is the total investment value in 2015
- tiv_2016 is the total investment value in 2016
- lat is the latitude of the policyholder's city
- lon is the longitude of the policyholder's city

Write a solution to report the sum of all total investment values in 2016
for all policyholders who:

1. Have the same tiv_2015 value as one or more other policyholders.
2. Are not located in the same city as any other policyholder.
   This means the pair (lat, lon) must be unique.

Round the result to two decimal places.

Example:
Input:
Insurance table:
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+

Output:
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+

APPROACH:
Use window functions.

For every row, calculate:
1. tiv_2015_count:
   how many policyholders have the same tiv_2015 value.

2. location_count:
   how many policyholders have the same (lat, lon) pair.

Then keep only rows where:
- tiv_2015_count > 1
- location_count = 1

Finally, sum tiv_2016 and round the result to two decimal places.

Time Complexity: O(n log n), depending on database implementation
Space Complexity: O(n), depending on database implementation

*/

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_2015_count,
        COUNT(*) OVER (PARTITION BY lat, lon) AS location_count
    FROM Insurance
) AS filtered_insurance
WHERE tiv_2015_count > 1
  AND location_count = 1;
