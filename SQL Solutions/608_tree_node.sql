/*
608. Tree Node
Difficulty: Medium
Link: https://leetcode.com/problems/tree-node/

PROBLEM:
Table: Tree

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+

id is the column with unique values for this table.
Each row contains information about a node id and its parent node id.

The given structure is always a valid tree.

Each node can be one of three types:

1. "Root":
   if the node is the root of the tree.
   The root node has p_id = NULL.

2. "Inner":
   if the node is neither a root nor a leaf.
   This means it has a parent and also has at least one child.

3. "Leaf":
   if the node has no children.

Write a solution to report the type of each node in the tree.

Return the result table in any order.

Example:
Input:
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | NULL |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

Output:
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+

APPROACH:
Use CASE with EXISTS.

For each node:
1. If p_id is NULL, the node is Root.
2. Else, if another row has p_id equal to this node's id,
   this node has at least one child, so it is Inner.
3. Otherwise, it has no children, so it is Leaf.

EXISTS checks whether the subquery returns at least one row.
The actual selected value inside EXISTS does not matter,
so SELECT 1 is commonly used.

Time Complexity: O(n^2) without indexes
Space Complexity: O(result size)

With an index on p_id, the EXISTS lookup can be much faster.

*/

SELECT
    parent.id,
    CASE
        WHEN parent.p_id IS NULL THEN 'Root'
        WHEN EXISTS (
            SELECT 1
            FROM Tree AS child
            WHERE child.p_id = parent.id
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree AS parent;
