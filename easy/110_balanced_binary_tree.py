"""

110. Balanced Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/balanced-binary-tree/

PROBLEM:
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than 1.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: True

Example 2:
Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
Output: False

Example 3:
Input: root = []
Output: True

APPROACH:
Use depth-first search.

For every node, we need to know two things:
1. The height of its subtree.
2. Whether its subtree is balanced.

Instead of checking height separately for every node, we calculate height
bottom-up.

If any subtree is not balanced, we return -1 as a signal.
Otherwise, we return the actual height of the subtree.

A node is balanced if:
abs(left_height - right_height) <= 1

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = get_height(node.left)
            if left_height == -1:
                return -1

            right_height = get_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return get_height(root) != -1


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
    print(solution.isBalanced(root))
    # True

    root = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(solution.isBalanced(root))
    # False

    root = build_tree([])
    print(solution.isBalanced(root))
    # True

    root = build_tree([1])
    print(solution.isBalanced(root))
    # True

    root = build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    print(solution.isBalanced(root))
    # False
