/*
1341. Movie Rating
Difficulty: Medium
Link: https://leetcode.com/problems/movie-rating/

PROBLEM:
Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+

movie_id is the primary key for this table.
title is the name of the movie.
Each movie has a unique title.

Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+

user_id is the primary key for this table.
name has unique values.

Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+

(movie_id, user_id) is the primary key for this table.
This table contains the rating of a movie by a user.
created_at is the review date.

Write a solution to:

1. Find the name of the user who rated the greatest number of movies.
   In case of a tie, return the lexicographically smaller user name.

2. Find the movie name with the highest average rating in February 2020.
   In case of a tie, return the lexicographically smaller movie title.

Return both answers in one column called results.

Example:
Output:
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+

APPROACH:
Use UNION ALL.

First query:
- Join Users with MovieRating.
- Group by user.
- Count how many movies each user rated.
- Sort by count descending.
- If there is a tie, sort by name ascending.
- Take the first row.

Second query:
- Join Movies with MovieRating.
- Filter only ratings from February 2020.
- Group by movie.
- Calculate average rating.
- Sort by average rating descending.
- If there is a tie, sort by title ascending.
- Take the first row.

UNION ALL combines both answers into one result column.

Time Complexity: O(n log n), because of grouping and sorting
Space Complexity: O(result size)

*/

(
    SELECT
        u.name AS results
    FROM Users AS u
    JOIN MovieRating AS mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
)

UNION ALL

(
    SELECT
        m.title AS results
    FROM Movies AS m
    JOIN MovieRating AS mr
        ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);
