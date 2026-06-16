"""

206. Reverse Linked List
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

PROBLEM:
Given the head of a singly linked list, reverse the list and return
the reversed list.

Example:
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

APPROACH:
Use three pointers:

prev    -> previous node
current -> current node we are processing
next_node -> temporarily stores the next node

For every node:
1. Save current.next in next_node.
2. Reverse the link: current.next = prev.
3. Move prev to current.
4. Move current to next_node.

At the end, prev becomes the new head of the reversed linked list.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev



# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    head = build_linked_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverseList(head)
    print(linked_list_to_list(reversed_head))
    # [5, 4, 3, 2, 1]

    head = build_linked_list([1, 2])
    reversed_head = solution.reverseList(head)
    print(linked_list_to_list(reversed_head))
    # [2, 1]

    head = build_linked_list([])
    reversed_head = solution.reverseList(head)
    print(linked_list_to_list(reversed_head))
    # []
