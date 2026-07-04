"""

100. Same Tree
Difficulty: Easy
Link: https://leetcode.com/problems/same-tree/

PROBLEM:
Given the roots of two binary trees p and q, check if they are the same.

Two binary trees are considered the same if:
1. They are structurally identical.
2. The nodes have the same values.

Example 1:
Input: p = [1, 2, 3], q = [1, 2, 3]
Output: True

Example 2:
Input: p = [1, 2], q = [1, None, 2]
Output: False

Example 3:
Input: p = [1, 2, 1], q = [1, 1, 2]
Output: False

APPROACH:
Use recursion.

For every pair of nodes p and q:
1. If both nodes are None, they are the same at this position.
2. If only one node is None, the trees are different.
3. If both nodes exist but their values are different, the trees are different.
4. Otherwise, recursively compare:
   - left subtree of p with left subtree of q
   - right subtree of p with right subtree of q

Time Complexity: O(n)
Space Complexity: O(h)

where:
n = number of nodes
h = height of the tree

In the worst case, h can be n for a skewed tree.

"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# --- Helper Function for Tests ---
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    p = build_tree([1, 2, 3])
    q = build_tree([1, 2, 3])
    print(solution.isSameTree(p, q))
    # True

    p = build_tree([1, 2])
    q = build_tree([1, None, 2])
    print(solution.isSameTree(p, q))
    # False

    p = build_tree([1, 2, 1])
    q = build_tree([1, 1, 2])
    print(solution.isSameTree(p, q))
    # False

    p = build_tree([])
    q = build_tree([])
    print(solution.isSameTree(p, q))
    # True
