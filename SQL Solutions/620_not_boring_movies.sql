/*
620. Not Boring Movies
Difficulty: Easy
Link: https://leetcode.com/problems/not-boring-movies/

PROBLEM:
Table: Cinema

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+

id is the primary key for this table.

Each row contains:
- movie id
- movie name
- description
- rating

rating is a float with 2 decimal places in the range [0, 10].

Write a solution to report movies with:
1. an odd-numbered id
2. a description that is not "boring"

Return the result table ordered by rating in descending order.

Example:
Input:
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+

Output:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+

APPROACH:
Use WHERE to filter rows.

A movie should be included if:
- id is odd
- description is not equal to "boring"

To check that id is odd, use:
id % 2 = 1

Then sort the result by rating in descending order.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(result size)

*/

SELECT
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;
