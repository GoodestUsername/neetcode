from collections import defaultdict, deque
from typing import List, Optional
import unittest


class ListNode:
    def __init__(self, x: int, next: "ListNode" = None):
        self.val = int(x)
        self.next = next

    @classmethod
    def from_List(cls, nums: List[int]):
        if len(nums) == 0:
            return None

        head = ListNode(nums[0], None)
        node = head

        for i in range(1, len(nums)):
            node.next = ListNode(nums[i], None)
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
    def run(self, head: Optional[ListNode]) -> bool:
        node = head

        visited = dict()
        while node:
            if node in visited:
                return True

            visited[node] = True
            node = node.next
        return False


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(
            answer,
            expected,
        )

    def test_cycle(self):
        self.e(
            args=ListNode.from_List([1, 2, 3]),
            expected=True,
        )

    def test_no_cycle(self):
        l2 = ListNode(2)
        l1 = ListNode(1, l2)

        self.e(
            args=l1,
            expected=False,
        )


if __name__ == "__main__":
    unittest.main()
