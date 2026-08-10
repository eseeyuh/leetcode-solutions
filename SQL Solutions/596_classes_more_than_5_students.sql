/*
596. Classes More Than 5 Students
Difficulty: Easy
Link: https://leetcode.com/problems/classes-more-than-5-students/

PROBLEM:
Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+

(student, class) is the primary key for this table.

Each row contains:
- student name
- class name

Write a solution to find all classes that have at least five students.

Return the result table in any order.

Example:
Input:
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+

Output:
+---------+
| class   |
+---------+
| Math    |
+---------+

Explanation:
Math has 6 students, so we include it.
Other classes have fewer than 5 students, so we do not include them.

APPROACH:
Use GROUP BY and HAVING.

GROUP BY class groups all rows by class.
COUNT(student) counts how many students are in each class.

Then HAVING COUNT(student) >= 5 keeps only classes with at least five students.

Time Complexity: O(n), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
