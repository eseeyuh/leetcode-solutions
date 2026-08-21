/*
602. Friend Requests II: Who Has the Most Friends
Difficulty: Medium
Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

PROBLEM:
Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+

(requester_id, accepter_id) is the primary key for this table.

This table contains:
- the ID of the user who sent the request
- the ID of the user who received the request
- the date when the request was accepted

Write a solution to find the person who has the most friends and their number
of friends.

The test cases are generated so that only one person has the most friends.

Example:
Input:
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+

Output:
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+

Explanation:
Person 3 is friends with people 1, 2, and 4.
So person 3 has 3 friends, which is the highest number.

APPROACH:
Use UNION ALL.

A friendship is counted for both people:
- requester_id gets one friend
- accepter_id gets one friend

So we create one column called id by combining:
1. requester_id values
2. accepter_id values

Then we group by id and count how many times each id appears.

Finally, sort by the count in descending order and return the first row.

Time Complexity: O(n log n), because of sorting
Space Complexity: O(n)

*/

SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
) AS all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;


/*
FOLLOW-UP:
If multiple people have the same maximum number of friends,
return all of them.

This version uses DENSE_RANK.
*/

/*
WITH friend_counts AS (
    SELECT
        id,
        COUNT(*) AS num
    FROM (
        SELECT requester_id AS id
        FROM RequestAccepted

        UNION ALL

        SELECT accepter_id AS id
        FROM RequestAccepted
    ) AS all_friends
    GROUP BY id
),
ranked_friend_counts AS (
    SELECT
        id,
        num,
        DENSE_RANK() OVER (ORDER BY num DESC) AS friend_rank
    FROM friend_counts
)
SELECT
    id,
    num
FROM ranked_friend_counts
WHERE friend_rank = 1;
*/
