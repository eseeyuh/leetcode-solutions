/*
550. Game Play Analysis IV
Difficulty: Medium
Link: https://leetcode.com/problems/game-play-analysis-iv/

PROBLEM:
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+

(player_id, event_date) is the primary key for this table.

Each row shows the activity of a player who logged in and played a number of games
on a certain date using a certain device.

Write a solution to report the fraction of players that logged in again on the day
after the day they first logged in.

The result should be rounded to 2 decimal places.

In other words:
1. Find each player's first login date.
2. Check whether the same player logged in again exactly one day later.
3. Divide the number of such players by the total number of players.

Example:
Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Output:
+----------+
| fraction |
+----------+
| 0.33     |
+----------+

Explanation:
Only player 1 logged in again on the day after their first login.
There are 3 total players.
So the fraction is 1 / 3 = 0.33.

APPROACH:
Use a subquery to find each player's first login date.

Then LEFT JOIN Activity again to check whether the player logged in on:

first_login + 1 day

COUNT(next_day_login.player_id) counts players who returned the next day.
COUNT(first_logins.player_id) counts all players.

Finally, divide these values and round to 2 decimal places.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(number of players)

*/

SELECT
    ROUND(
        COUNT(next_day_login.player_id) / COUNT(first_logins.player_id),
        2
    ) AS fraction
FROM (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) AS first_logins
LEFT JOIN Activity AS next_day_login
    ON first_logins.player_id = next_day_login.player_id
   AND DATEDIFF(next_day_login.event_date, first_logins.first_login) = 1;
