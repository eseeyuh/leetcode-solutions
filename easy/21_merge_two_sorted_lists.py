"""

21. Merge Two Sorted Lists
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

PROBLEM:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

APPROACH:
Use a dummy node to simplify building the merged list.

We compare the current nodes of list1 and list2.
The smaller node is attached to the merged list.
Then we move forward in the list from which we took the node.

When one list becomes empty, we attach the remaining part of the other list.

Time Complexity: O(n + m)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        cur = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        cur.next = list1 if list1 is not None else list2

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

    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))
    # [1, 1, 2, 3, 4, 4]

    list1 = build_linked_list([])
    list2 = build_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))
    # []

    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))
    # [0]

    list1 = build_linked_list([2])
    list2 = build_linked_list([1])
    merged = solution.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))
    # [1, 2]
