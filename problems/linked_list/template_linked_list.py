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
        return None


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

    def test_dup(self):
        self.e(
            args=dict(l1=Node.from_List([1, 2, 3]), l2=Node.from_List([4, 5, 6])),
            expected=Node.from_List([5, 7, 9]),
        )


if __name__ == "__main__":
    unittest.main()
