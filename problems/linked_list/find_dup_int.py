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
    # failed attempt
    # def run(self, nums: List[int]) -> int:
    #     if len(nums) == 2:
    #         return nums[0]

    #     i = 0
    #     hare = 1
    #     while nums[i] != nums[hare]:
    #         hare += 2
    #         hare = hare % (len(nums) - 1)

    #         if (i + 1) >= len(nums):
    #             i = 0
    #         else:
    #             i += 1

    #         if hare == i:
    #             hare = i + 1
    #     return nums[i]

    # O(n) space complexity solution
    # def run(self, nums: List[int]) -> int:
    #     seen = dict()
    #     for num in nums:
    #         if num in seen:
    #              return True
    #         seen[num] = True

    #     return False

    # actual solution
    # uses the fact that the numbers can be indexes without overflowing
    def run(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


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

    def test_dup_middle(self):
        self.e(
            args=[1, 2, 3, 2, 2],
            expected=2,
        )

    def test_dup_end(self):
        self.e(
            args=[1, 2, 3, 4, 4],
            expected=4,
        )


if __name__ == "__main__":
    unittest.main()
