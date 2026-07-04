"""

19. Remove Nth Node From End of List
Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

PROBLEM:
Given the head of a linked list, remove the nth node from the end
of the list and return its head.

Example 1:
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1, 2], n = 1
Output: [1]

APPROACH:
Use two pointers: fast and slow.

Create a dummy node before head.
This helps handle the case where we need to remove the first node.

Move fast n + 1 steps forward.
Then move both fast and slow together until fast reaches the end.

At that point, slow is right before the node we need to remove.
So we skip that node:

slow.next = slow.next.next

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

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

    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))
    # [1, 2, 3, 5]

    head = build_linked_list([1])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))
    # []

    head = build_linked_list([1, 2])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))
    # [1]

    head = build_linked_list([1, 2])
    result = solution.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))
    # [2]
