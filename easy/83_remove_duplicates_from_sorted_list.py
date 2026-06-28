"""

83. Remove Duplicates from Sorted List
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

PROBLEM:
Given the head of a sorted linked list, delete all duplicates
so that each element appears only once.

Return the linked list sorted as well.

Example 1:
Input: head = [1, 1, 2]
Output: [1, 2]

Example 2:
Input: head = [1, 1, 2, 3, 3]
Output: [1, 2, 3]

APPROACH:
Because the linked list is already sorted, duplicates will always be
next to each other.

Use one pointer called current.

While current and current.next exist:
1. If current.val is equal to current.next.val, skip current.next.
2. Otherwise, move current forward.

This removes duplicate nodes in-place.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


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

    head = build_linked_list([1, 1, 2])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # [1, 2]

    head = build_linked_list([1, 1, 2, 3, 3])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # [1, 2, 3]

    head = build_linked_list([])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # []

    head = build_linked_list([1, 1, 1])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # [1]

    head = build_linked_list([1, 2, 3])
    result = solution.deleteDuplicates(head)
    print(linked_list_to_list(result))
    # [1, 2, 3]
