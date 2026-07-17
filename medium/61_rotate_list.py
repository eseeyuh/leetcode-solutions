"""

61. Rotate List
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-list/

PROBLEM:
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Example 2:
Input: head = [0, 1, 2], k = 4
Output: [2, 0, 1]

APPROACH:
First, find the length of the linked list and the tail node.

If k is larger than the length of the list, rotating by k is the same as
rotating by k % length.

Then connect the tail to the head to temporarily make the list circular.

After that, find the new tail:
length - k - 1 steps from the original head.

The node after the new tail becomes the new head.
Finally, break the circle by setting new_tail.next = None.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if k == 0:
            return head

        tail.next = head

        steps_to_new_tail = length - k - 1
        new_tail = head

        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


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
    result = solution.rotateRight(head, 2)
    print(linked_list_to_list(result))
    # [4, 5, 1, 2, 3]

    head = build_linked_list([0, 1, 2])
    result = solution.rotateRight(head, 4)
    print(linked_list_to_list(result))
    # [2, 0, 1]

    head = build_linked_list([])
    result = solution.rotateRight(head, 0)
    print(linked_list_to_list(result))
    # []

    head = build_linked_list([1])
    result = solution.rotateRight(head, 99)
    print(linked_list_to_list(result))
    # [1]

    head = build_linked_list([1, 2])
    result = solution.rotateRight(head, 2)
    print(linked_list_to_list(result))
    # [1, 2]
