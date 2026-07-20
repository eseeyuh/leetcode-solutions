"""

23. Merge k Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

PROBLEM:
You are given an array of k linked lists.

Each linked list is sorted in ascending order.

Merge all linked lists into one sorted linked list and return it.

Example 1:
Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]

Explanation:
The linked lists are:
[
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]

After merging:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

APPROACH:
Use a min-heap.

Since every linked list is already sorted, the smallest available node
must be one of the current heads of the lists.

Steps:
1. Add the head of every non-empty linked list to the heap.
2. Pop the smallest node from the heap.
3. Attach it to the merged linked list.
4. If that node has a next node, push the next node into the heap.
5. Repeat until the heap is empty.

We use a counter in the heap tuple to avoid comparing ListNode objects
directly when two nodes have the same value.

Time Complexity: O(N log k)
Space Complexity: O(k)

where:
N = total number of nodes across all linked lists
k = number of linked lists

"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        counter = 0

        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, counter, head))
                counter += 1

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            _, _, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

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


def build_lists(list_of_values):
    return [build_linked_list(values) for values in list_of_values]


# --- Tests ---
if __name__ == "__main__":
    solution = Solution()

    lists = build_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
    merged = solution.mergeKLists(lists)
    print(linked_list_to_list(merged))
    # [1, 1, 2, 3, 4, 4, 5, 6]

    lists = build_lists([])
    merged = solution.mergeKLists(lists)
    print(linked_list_to_list(merged))
    # []

    lists = build_lists([[]])
    merged = solution.mergeKLists(lists)
    print(linked_list_to_list(merged))
    # []

    lists = build_lists([[1], [0]])
    merged = solution.mergeKLists(lists)
    print(linked_list_to_list(merged))
    # [0, 1]
