from collections import defaultdict, deque
from typing import List, Optional
import unittest


class Node:
    def __init__(self, x: int, next: "Node" = None):
        self.val = int(x)
        self.next = next

    @classmethod
    def from_List(cls, nums: List[int]):
        if len(nums) == 0:
            return None

        head = Node(nums[0], None)
        node = head

        for i in range(1, len(nums)):
            node.next = Node(nums[i], None)
            node = node.next

        return head

    def get_next_val(self):
        if self.next:
            return self.next.val
        return None

    def to_array(self):
        if self == None:
            return []

        val_list = []

        node = self
        while node:
            val_list.append(node.val)
            node = node.next

        return val_list


class Solution:
    def run(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        head = Node(0)
        node = head
        carry = False
        while l1 or l2:
            cur_total = 0

            if l1 and l2:
                cur_total = l1.val + l2.val
            else:
                cur_total = l1.val if l1 else l2.val

            if carry:
                cur_total += 1

            carry = cur_total >= 10

            last_digit = cur_total % 10

            node.next = Node(last_digit)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            node.next = Node(1)

        return head.next


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(
            answer.to_array() if answer != None else None,
            expected.to_array() if expected != None else None,
        )

    def test_no_carry(self):
        self.e(
            args=dict(l1=Node.from_List([1, 2, 3]), l2=Node.from_List([4, 5, 6])),
            expected=Node.from_List([5, 7, 9]),
        )

    def test_carry(self):
        self.e(
            args=dict(l1=Node.from_List([9]), l2=Node.from_List([9])),
            expected=Node.from_List([8, 1]),
        )


if __name__ == "__main__":
    unittest.main()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# looks cleaner
# class Solution:
#     def addTwoNumbers(
#         self, l1: Optional[ListNode], l2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         dummy = ListNode()
#         cur = dummy

#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0

#             # new digit
#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)

#             # update ptrs
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next
