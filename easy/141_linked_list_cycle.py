"""

141. Linked List Cycle
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/

PROBLEM:
Given head, the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if some node in the list can be reached again
by continuously following the next pointer.

Internally, pos is used to denote the index of the node that the tail connects to.
However, pos is not passed as a parameter.

Return True if there is a cycle in the linked list.
Otherwise, return False.

Example 1:
Input: head = [3, 2, 0, -4], pos = 1
Output: True

Explanation:
There is a cycle where the tail connects to the node at index 1.

Example 2:
Input: head = [1, 2], pos = 0
Output: True

Explanation:
There is a cycle where the tail connects to the node at index 0.

Example 3:
Input: head = [1], pos = -1
Output: False

Explanation:
There is no cycle in the linked list.

APPROACH:
Use Floyd's Cycle Detection Algorithm.

We use two pointers:
1. slow moves one step at a time.
2. fast moves two steps at a time.

If there is no cycle, fast will eventually reach the end of the linked list.

If there is a cycle, fast will eventually meet slow inside the cycle.

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# --- Helper Function for Tests ---
def build_linked_list_with_cycle(values, pos):
    if not values:
        return None

    nodes = [ListNode(value) for value in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    head = build_linked_list_with_cycle([3, 2, 0, -4], 1)
    print(solution.hasCycle(head))
    # True

    head = build_linked_list_with_cycle([1, 2], 0)
    print(solution.hasCycle(head))
    # True

    head = build_linked_list_with_cycle([1], -1)
    print(solution.hasCycle(head))
    # False

    head = build_linked_list_with_cycle([], -1)
    print(solution.hasCycle(head))
    # False
