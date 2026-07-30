/*
182. Duplicate Emails
Difficulty: Easy
Link: https://leetcode.com/problems/duplicate-emails/

PROBLEM:
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+

id is the primary key for this table.
Each row contains an email.
Emails do not contain uppercase letters.
The email field is guaranteed to be not NULL.

Write a solution to report all duplicate emails.

Return the result table in any order.

Example:
Input:
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

Output:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Explanation:
a@b.com appears two times.

APPROACH:
Use GROUP BY and HAVING.

GROUP BY email groups rows with the same email together.
COUNT(*) counts how many times each email appears.

If COUNT(*) > 1, the email is duplicated.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
