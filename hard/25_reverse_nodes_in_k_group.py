"""

25. Reverse Nodes in k-Group
Difficulty: Hard
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

PROBLEM:
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.

If the number of nodes is not a multiple of k, then the left-out nodes at the end
should remain as they are.

You may not alter the values in the list's nodes.
Only the nodes themselves may be changed.

Example 1:
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]

Example 2:
Input: head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]

APPROACH:
Use iterative linked list reversal in groups of size k.

We use a dummy node before the head to make pointer changes easier.

For every group:
1. Check whether there are at least k nodes left.
2. If not, leave the remaining nodes unchanged.
3. Reverse exactly k nodes.
4. Connect the previous part of the list to the reversed group.
5. Move to the next group.

This solution changes only node links, not node values.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth_node(group_prev, k)

            if not kth:
                break

            group_next = kth.next

            prev = group_next
            current = group_prev.next

            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            old_group_head = group_prev.next
            group_prev.next = kth
            group_prev = old_group_head

        return dummy.next

    def get_kth_node(self, current: ListNode, k: int) -> Optional[ListNode]:

        while current and k > 0:
            current = current.next
            k -= 1

        return current


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
    result = solution.reverseKGroup(head, 2)
    print(linked_list_to_list(result))
    # [2, 1, 4, 3, 5]

    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseKGroup(head, 3)
    print(linked_list_to_list(result))
    # [3, 2, 1, 4, 5]

    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseKGroup(head, 1)
    print(linked_list_to_list(result))
    # [1, 2, 3, 4, 5]

    head = build_linked_list([1, 2])
    result = solution.reverseKGroup(head, 2)
    print(linked_list_to_list(result))
    # [2, 1]
