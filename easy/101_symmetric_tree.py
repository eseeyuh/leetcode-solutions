"""

101. Symmetric Tree
Difficulty: Easy
Link: https://leetcode.com/problems/symmetric-tree/

PROBLEM:
Given the root of a binary tree, check whether it is a mirror of itself.

A binary tree is symmetric if its left subtree is a mirror of its right subtree.

Example 1:
Input: root = [1, 2, 2, 3, 4, 4, 3]
Output: True

Example 2:
Input: root = [1, 2, 2, None, 3, None, 3]
Output: False

APPROACH:
Use recursion.

Two subtrees are mirrors if:
1. Both nodes are None.
2. Both nodes exist and have the same value.
3. The left child of the first node matches the right child of the second node.
4. The right child of the first node matches the left child of the second node.

This solution also includes an iterative version as an extra method.

Time Complexity: O(n)
Space Complexity: O(h) for recursion, where h is the height of the tree

For the iterative version:
Time Complexity: O(n)
Space Complexity: O(n)

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
            if not left_node and not right_node:
                return True

            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            return (
                is_mirror(left_node.left, right_node.right)
                and is_mirror(left_node.right, right_node.left)
            )

        return is_mirror(root.left, root.right)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:

        queue = deque([(root.left, root.right)])

        while queue:
            left_node, right_node = queue.popleft()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            queue.append((left_node.left, right_node.right))
            queue.append((left_node.right, right_node.left))

        return True


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

    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(solution.isSymmetric(root))
    # True

    root = build_tree([1, 2, 2, None, 3, None, 3])
    print(solution.isSymmetric(root))
    # False

    root = build_tree([1])
    print(solution.isSymmetric(root))
    # True

    root = build_tree([1, 2, 2, 3, None, None, 3])
    print(solution.isSymmetricIterative(root))
    # True
