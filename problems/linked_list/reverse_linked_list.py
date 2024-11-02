from typing import List, Optional
import unittest
import sys

sys.tracebacklimit = 0


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def run(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        node = ListNode(head.val, next=None)
        head = head.next
        while head != None:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node


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
        answer = self.linked_list_values(self.solution.run(args))

        self.assertEqual(answer, expected)

    def test_reverse(self):
        self.e(
            args=ListNode(0, ListNode(1, ListNode(2, ListNode(3, None)))),
            expected=[3, 2, 1, 0],
        )

    def test_empty(self):
        self.e(args=None, expected=[])


if __name__ == "__main__":
    unittest.main()
