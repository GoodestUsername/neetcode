from typing import List, Optional
import unittest
import sys

sys.tracebacklimit = 0


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def listToTree(cls, nums: List[int]):
        if not nums:
            return None
        root = TreeNode(nums[0])
        q = [root]
        i = 1
        while i < len(nums):
            curr = q.pop(0)
            if i < len(nums):
                curr.left = TreeNode(nums[i])
                q.append(curr.left)
                i += 1
            if i < len(nums):
                curr.right = TreeNode(nums[i])
                q.append(curr.right)
                i += 1
        return root

    @classmethod
    def treeToList(cls, root) -> List[int]:
        if not root:
            return []

        nums = [root.val]
        q = [root]
        while len(q) > 0:
            cur = q.pop(0)
            if cur.left:
                nums.append(cur.left.val)
                q.append(cur.left)
            if cur.right:
                nums.append(cur.right.val)
                q.append(cur.right)
        return nums


class Solution:
    def run(self, root: TreeNode) -> Optional[TreeNode]:

        return TreeNode.treeToList(root)


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def test_self(self):
        self.e(
            args=TreeNode.listToTree(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            ),
            expected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        )


if __name__ == "__main__":
    unittest.main()
