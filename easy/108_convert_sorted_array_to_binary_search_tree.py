"""

108. Convert Sorted Array to Binary Search Tree
Difficulty: Easy
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

PROBLEM:
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, None, 5]

Example 2:
Input: nums = [1, 3]
Output: [3, 1]

APPROACH:
Use recursion.

Because nums is sorted, the middle element is the best root for a balanced BST.

For every subarray:
1. Pick the middle element as the root.
2. Recursively build the left subtree from the left half.
3. Recursively build the right subtree from the right half.

This keeps the tree height-balanced.

Time Complexity: O(n)
Space Complexity: O(log n) for recursion stack in a balanced tree

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)

            return root

        return build_tree(0, len(nums) - 1)


# --- Helper Function for Tests ---
def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    root = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(tree_to_list(root))
    # [0, -10, 5, None, -3, None, 9]

    root = solution.sortedArrayToBST([1, 3])
    print(tree_to_list(root))
    # [1, None, 3]

    root = solution.sortedArrayToBST([])
    print(tree_to_list(root))
    # []

    root = solution.sortedArrayToBST([1])
    print(tree_to_list(root))
    # [1]
