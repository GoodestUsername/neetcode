from collections import deque
from typing import List, Optional
import unittest
import sys

sys.tracebacklimit = 0


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
    def run(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        reverse_stack = deque()
        i = 1

        node = head
        while node != None:
            reverse_stack.appendleft(node)
            if (len(reverse_stack)) > (n + 1):
                reverse_stack.pop()

            node = node.next
            i += 1
        if n >= len(reverse_stack):
            reverse_stack[0].next = None
            return head.next

        reverse_stack[n].next = reverse_stack[n].next.next
        return head


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
        answer = self.linked_list_values(self.solution.run(**args))

        self.assertEqual(answer, expected)

    def test_small(self):
        self.e(
            args=dict(
                head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))), n=2
            ),
            expected=[1, 2, 4],
        )

    def test_big(self):
        self.e(
            args=dict(
                head=ListNode(
                    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))
                ),
                n=2,
            ),
            expected=[1, 2, 3, 5],
        )

    def test_lowest(self):
        self.e(
            args=dict(
                head=ListNode(5, None),
                n=1,
            ),
            expected=[],
        )

    def test_overflow(self):
        self.e(
            args=dict(
                head=ListNode(1, ListNode(2, None)),
                n=2,
            ),
            expected=[2],
        )


if __name__ == "__main__":
    unittest.main()
    # remove from beginning
    # def run(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     if head == None or head.next == None:
    #         return None
    #     i = 0

    #     node = head
    #     while (n - 1) > i:
    #         if node.next == None:
    #             node = head
    #         else:
    #             node = node.next
    #         i += 1

    #     if node.next == None:
    #         return node

    #     node.next = node.next.next
    #     return head
