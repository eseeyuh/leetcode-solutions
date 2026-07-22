"""

111. Minimum Depth of Binary Tree
Difficulty: Easy
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

PROBLEM:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

A leaf is a node with no children.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 2

Example 2:
Input: root = [2, null, 3, null, 4, null, 5, null, 6]
Output: 5

APPROACH:
Use breadth-first search.

Since we need the shortest path from the root to the nearest leaf,
BFS is a natural choice.

BFS visits the tree level by level.
The first leaf node we find is guaranteed to be the nearest leaf.

Steps:
1. If root is None, return 0.
2. Add the root to the queue with depth 1.
3. Pop nodes from the queue.
4. If the current node is a leaf, return its depth.
5. Otherwise, add its existing children to the queue with depth + 1.

Time Complexity: O(n)
Space Complexity: O(w)

where:
n = number of nodes in the tree
w = maximum width of the tree

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
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return 0


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
    print(solution.minDepth(root))
    # 2

    root = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    print(solution.minDepth(root))
    # 5

    root = build_tree([])
    print(solution.minDepth(root))
    # 0

    root = build_tree([1])
    print(solution.minDepth(root))
    # 1

    root = build_tree([1, 2, 3, 4, 5])
    print(solution.minDepth(root))
    # 2
