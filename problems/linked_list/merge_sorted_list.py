from collections import deque
from typing import List, Optional
import unittest
import sys

# sys.tracebacklimit = 0


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_values(head: Optional[ListNode]):
    vals = []
    while head != None:
        vals.append(head.val)
        head = head.next
    return vals


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def run(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return head

        linked_list_stack = deque()

        while head:
            linked_list_stack.append(head)
            temp = head.next
            head.next = None
            head = temp

        list_len = len(linked_list_stack)

        for i in range((list_len // 2)):
            linked_list_stack[i].next = linked_list_stack[list_len - 1 - i]
            linked_list_stack[list_len - 1 - i].next = linked_list_stack[i + 1]

        linked_list_stack[i + 1].next = None


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def linked_list_values(self, head: Optional[ListNode]):
        vals = []
        while head != None:
            vals.append(head.val)
            head = head.next
        return vals

    def e(self, args, expected):
        self.solution.run(args)
        answer = self.linked_list_values(args)

        self.assertEqual(answer, expected)

    def test_reverse(self):
        self.e(
            args=ListNode(2, ListNode(4, ListNode(6, ListNode(8, None)))),
            expected=[2, 8, 4, 6],
        )

    def test_empty(self):
        self.e(
            args=ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10, None))))),
            expected=[2, 10, 4, 8, 6],
        )


if __name__ == "__main__":
    unittest.main()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# space optimal solution
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         second = slow.next
#         prev = slow.next = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp

#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2
