"""

160. Intersection of Two Linked Lists
Difficulty: Easy
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

PROBLEM:
Given the heads of two singly linked lists headA and headB,
return the node at which the two lists intersect.

If the two linked lists have no intersection, return None.

The lists must retain their original structure after the function returns.

Important:
The intersection is based on node reference, not node value.

For example, if two nodes have the same value but are different objects,
they are not considered an intersection.

APPROACH:
Use two pointers.

Start:
- itrA at headA
- itrB at headB

Move both pointers one step at a time.

When itrA reaches the end of list A, redirect it to headB.
When itrB reaches the end of list B, redirect it to headA.

Why this works:
If the lists intersect, both pointers will travel the same total distance:

lengthA + lengthB

After switching lists, the longer-list pointer loses its extra distance,
and both pointers arrive at the intersection node at the same time.

If the lists do not intersect, both pointers will eventually become None
at the same time, and the loop stops.

Time Complexity: O(m + n)
Space Complexity: O(1)

where:
m = length of list A
n = length of list B

"""

from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:

        itrA = headA
        itrB = headB

        while itrA is not itrB:
            if itrA:
                itrA = itrA.next
            else:
                itrA = headB

            if itrB:
                itrB = itrB.next
            else:
                itrB = headA

        return itrA


# --- Helpers for tests ---
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def get_tail(head):
    current = head

    while current and current.next:
        current = current.next

    return current


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    # Example with intersection:
    # A: 4 -> 1 \
    #           8 -> 4 -> 5
    # B: 5 -> 6 -> 1 /
    common = build_linked_list([8, 4, 5])

    headA = build_linked_list([4, 1])
    get_tail(headA).next = common

    headB = build_linked_list([5, 6, 1])
    get_tail(headB).next = common

    intersection = solution.getIntersectionNode(headA, headB)
    print(intersection.val if intersection else None)
    # 8

    # Example without intersection:
    headA = build_linked_list([1, 2, 3])
    headB = build_linked_list([4, 5, 6])

    intersection = solution.getIntersectionNode(headA, headB)
    print(intersection.val if intersection else None)
    # None

    # Same values, but no shared nodes:
    headA = build_linked_list([1, 2])
    headB = build_linked_list([1, 2])

    intersection = solution.getIntersectionNode(headA, headB)
    print(intersection.val if intersection else None)
    # None
