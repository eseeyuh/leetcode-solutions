/*
196. Delete Duplicate Emails
Difficulty: Easy
Link: https://leetcode.com/problems/delete-duplicate-emails/

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

Write a solution to delete all duplicate emails, keeping only one unique email
with the smallest id.

Important:
This problem requires a DELETE statement, not a SELECT statement.

Example:
Input:
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Output:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

Explanation:
john@example.com appears twice.
We keep the row with the smallest id = 1 and delete the duplicate row with id = 3.

APPROACH:
Use a self join.

We compare the Person table with itself:

- p1 is the row that may be deleted.
- p2 is another row with the same email.

If p1.email = p2.email and p1.id > p2.id,
then p1 is a duplicate with a larger id.

So we delete p1.

Time Complexity: O(n^2), depending on database indexing
Space Complexity: O(1)

*/

DELETE p1
FROM Person AS p1
JOIN Person AS p2
    ON p1.email = p2.email
   AND p1.id > p2.id;
