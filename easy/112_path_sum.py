"""

112. Path Sum
Difficulty: Easy
Link: https://leetcode.com/problems/path-sum/

PROBLEM:
Given the root of a binary tree and an integer targetSum, return True if the
tree has a root-to-leaf path such that adding up all the values along the path
equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1],
targetSum = 22
Output: True

Explanation:
The path 5 -> 4 -> 11 -> 2 has sum 22.

Example 2:
Input: root = [1, 2, 3], targetSum = 5
Output: False

Explanation:
There are two root-to-leaf paths:
1 -> 2 = 3
1 -> 3 = 4

There is no root-to-leaf path with sum 5.

Example 3:
Input: root = [], targetSum = 0
Output: False

APPROACH:
Use depth-first search.

At every node, subtract the node value from targetSum.

When we reach a leaf node, we check whether the remaining target sum is equal
to the leaf value.

If yes, there is a valid root-to-leaf path.
If not, we continue checking the left and right subtrees.

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining_sum = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining_sum)
            or self.hasPathSum(root.right, remaining_sum)
        )


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

    root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print(solution.hasPathSum(root, 22))
    # True

    root = build_tree([1, 2, 3])
    print(solution.hasPathSum(root, 5))
    # False

    root = build_tree([])
    print(solution.hasPathSum(root, 0))
    # False

    root = build_tree([1, 2])
    print(solution.hasPathSum(root, 1))
    # False

    root = build_tree([1, 2])
    print(solution.hasPathSum(root, 3))
    # True
