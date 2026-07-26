/*
175. Combine Two Tables
Difficulty: Easy
Link: https://leetcode.com/problems/combine-two-tables/

PROBLEM:
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+

personId is the primary key for this table.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+

addressId is the primary key for this table.

Write a solution to report:
- firstName
- lastName
- city
- state

for each person in the Person table.

If a person's address is not present in the Address table,
return NULL for city and state.

APPROACH:
Use LEFT JOIN.

We need all rows from Person.
If a matching personId exists in Address, we include city and state.
If there is no matching address, SQL automatically returns NULL
for Address columns.

Time Complexity: O(n + m), depending on database indexing
Space Complexity: O(result size)

*/

SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
LEFT JOIN Address
    ON Person.personId = Address.personId;
