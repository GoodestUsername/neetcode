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
        while i < len(nums) and len(q):
            curr = q.pop(0)
            if i < len(nums):
                if nums[i] != None:
                    curr.left = TreeNode(nums[i])
                    q.append(curr.left)
                i += 1
            if i < len(nums):
                if nums[i] != None:
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
        if not root:
            return None
        self.run(root.left)
        self.run(root.right)

        temp = root.right
        root.right = root.left
        root.left = temp

        return root


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(TreeNode.treeToList(answer), TreeNode.treeToList(expected))

    def test_avg(self):
        self.e(
            args=TreeNode.listToTree([1, 2, 3, 4, 5, 6, 7]),
            expected=TreeNode.listToTree([1, 3, 2, 7, 6, 5, 4]),
        )

    def test_min(self):
        self.e(
            args=TreeNode.listToTree([3, 2, 1]),
            expected=TreeNode.listToTree([3, 1, 2]),
        )


if __name__ == "__main__":
    unittest.main()
