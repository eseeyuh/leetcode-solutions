"""

145. Binary Tree Postorder Traversal
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

PROBLEM:
Given the root of a binary tree, return the postorder traversal of its nodes'
values.

Postorder traversal means:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root node.

Example 1:
Input: root = [1, null, 2, 3]
Output: [3, 2, 1]

Example 2:
Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [4, 6, 7, 5, 2, 9, 8, 3, 1]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

FOLLOW-UP:
Recursive solution is simple.
This file uses an iterative solution.

APPROACH:
Use a stack.

Postorder is:
left -> right -> root

A useful trick is to process nodes in this order:
root -> right -> left

Then reverse the result at the end.

Steps:
1. Put root into the stack.
2. Pop a node from the stack.
3. Add its value to result.
4. Push left child first.
5. Push right child second.
6. Reverse result.

Because the stack is LIFO, pushing left first and right second makes the
right child processed before the left child.

The result before reversing is:
root -> right -> left

After reversing, it becomes:
left -> right -> root

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return result[::-1]


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
    print(solution.postorderTraversal(root))
    # [3, 2, 1]

    root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
    print(solution.postorderTraversal(root))
    # [4, 6, 7, 5, 2, 9, 8, 3, 1]

    root = build_tree([])
    print(solution.postorderTraversal(root))
    # []

    root = build_tree([1])
    print(solution.postorderTraversal(root))
    # [1]
