"""

24. Swap Nodes in Pairs
Difficulty: Medium
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

PROBLEM:
Given a linked list, swap every two adjacent nodes and return its head.

You must solve the problem without modifying the values in the nodes.
Only the nodes themselves may be changed.

Example 1:
Input: head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1, 2, 3]
Output: [2, 1, 3]

APPROACH:
Use a dummy node before the head.

For each pair:
1. first points to the first node in the pair.
2. second points to the second node in the pair.
3. Swap the links between prev, first, and second.
4. Move prev to the end of the swapped pair.

This changes only node connections, not node values.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next


# --- Helper Functions for Tests ---
def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    head = build_linked_list([1, 2, 3, 4])
    result = solution.swapPairs(head)
    print(linked_list_to_list(result))
    # [2, 1, 4, 3]

    head = build_linked_list([])
    result = solution.swapPairs(head)
    print(linked_list_to_list(result))
    # []

    head = build_linked_list([1])
    result = solution.swapPairs(head)
    print(linked_list_to_list(result))
    # [1]

    head = build_linked_list([1, 2, 3])
    result = solution.swapPairs(head)
    print(linked_list_to_list(result))
    # [2, 1, 3]
