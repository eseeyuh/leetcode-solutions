/*
178. Rank Scores
Difficulty: Medium
Link: https://leetcode.com/problems/rank-scores/

PROBLEM:
Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+

id is the primary key for this table.
Each row contains the score of a game.

Write a solution to find the rank of the scores.

Ranking rules:
1. Scores should be ranked from highest to lowest.
2. If there is a tie, equal scores should have the same rank.
3. After a tie, the next rank should be the next consecutive integer.
   There should be no gaps between ranks.

Return the result table ordered by score in descending order.

Example:
Input:
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

Output:
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

APPROACH:
Use DENSE_RANK.

DENSE_RANK gives the same rank to equal scores.
After a tie, it continues with the next consecutive rank.

For example:
4.00 -> rank 1
4.00 -> rank 1
3.85 -> rank 2
3.65 -> rank 3
3.65 -> rank 3
3.50 -> rank 4

This matches the requirement because there are no gaps between ranks.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(n), depending on the database engine

*/

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
