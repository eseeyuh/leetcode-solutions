"""

144. Binary Tree Preorder Traversal
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

PROBLEM:
Given the root of a binary tree, return the preorder traversal of its nodes'
values.

Preorder traversal means:
1. Visit the root node.
2. Traverse the left subtree.
3. Traverse the right subtree.

Example 1:
Input: root = [1, null, 2, 3]
Output: [1, 2, 3]

Example 2:
Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

APPROACH:
Use depth-first search.

In preorder traversal, we process the current node first, then go to the left
subtree, and then go to the right subtree.

So for every node:
1. Add node.val to the result.
2. Recursively visit node.left.
3. Recursively visit node.right.

Time Complexity: O(n)
Space Complexity: O(h)

where:
n = number of nodes in the tree
h = height of the tree

"""

from collections import deque
from typing import List, Optional


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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result


# --- Helper Function for Tests ---
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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

    root = build_tree([1, None, 2, 3])
    print(solution.preorderTraversal(root))
    # [1, 2, 3]

    root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print(solution.preorderTraversal(root))
    # [1, 2, 4, 5, 6, 7, 3, 8, 9]

    root = build_tree([])
    print(solution.preorderTraversal(root))
    # []

    root = build_tree([1])
    print(solution.preorderTraversal(root))
    # [1]
