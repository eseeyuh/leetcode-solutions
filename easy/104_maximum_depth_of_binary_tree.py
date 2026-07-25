"""

104. Maximum Depth of Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

PROBLEM:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3

Example 2:
Input: root = [1, null, 2]
Output: 2

APPROACH:
Use depth-first search.

For every node:
1. Find the maximum depth of the left subtree.
2. Find the maximum depth of the right subtree.
3. Take the larger one and add 1 for the current node.

If the node is None, its depth is 0.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


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

    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(solution.maxDepth(root))
    # 3

    root = build_tree([1, None, 2])
    print(solution.maxDepth(root))
    # 2

    root = build_tree([])
    print(solution.maxDepth(root))
    # 0

    root = build_tree([1])
    print(solution.maxDepth(root))
    # 1

    root = build_tree([1, 2, 3, 4, 5])
    print(solution.maxDepth(root))
    # 3
