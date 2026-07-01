"""

94. Binary Tree Inorder Traversal
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

PROBLEM:
Given the root of a binary tree, return the inorder traversal
of its nodes' values.

Inorder traversal means:
1. Visit the left subtree.
2. Visit the current node.
3. Visit the right subtree.

Example 1:
Input: root = [1, None, 2, 3]
Output: [1, 3, 2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

FOLLOW-UP:
Recursive solution is simple, but this solution uses an iterative approach.

APPROACH:
Use a stack.

We start from the root and keep going left, pushing every node into the stack.
When there is no more left child:
1. Pop the last node from the stack.
2. Add its value to the result.
3. Move to its right child.

This simulates the recursive inorder traversal without recursion.

Time Complexity: O(n)
Space Complexity: O(n)

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result


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

    root = build_tree([1, None, 2, 3])
    print(solution.inorderTraversal(root))
    # [1, 3, 2]

    root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print(solution.inorderTraversal(root))
    # [4, 2, 6, 5, 7, 1, 3, 9, 8]

    root = build_tree([])
    print(solution.inorderTraversal(root))
    # []

    root = build_tree([1])
    print(solution.inorderTraversal(root))
    # [1]
