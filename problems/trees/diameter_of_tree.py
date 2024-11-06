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
    # couldn't figure out what the question was asking for, this is the guy's solution
    def run(self, root: TreeNode) -> Optional[TreeNode]:
        if not root:
            return 0

        res = 0

        def depthSearch(root) -> int:
            if not root:
                return 0

            nonlocal res
            l = depthSearch(root.left)
            r = depthSearch(root.right)
            res = max(res, l + r)
            return max(l, r) + 1

        depthSearch(root)

        return res


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

    def test_long_branch(self):
        self.e(
            args=TreeNode.listToTree([1, 2, 3, 4, 5]),
            expected=3,
        )

    def test_missing_leaf_long_branch(self):
        self.e(
            args=TreeNode.listToTree([1, None, 2, 3, 4, 5]),
            expected=3,
        )

    def test_empty(self):
        self.e(
            args=TreeNode.listToTree([]),
            expected=0,
        )

    def test_min_tree(self):
        self.e(
            args=TreeNode.listToTree([1, 2]),
            expected=1,
        )

    def test_small_tree(self):
        self.e(
            args=TreeNode.listToTree([1, 2, 3]),
            expected=2,
        )

    def test_missing_left(self):
        self.e(args=TreeNode.listToTree([2, 3, None, 1]), expected=2)

    def test_triangle(self):
        self.e(args=TreeNode.listToTree([3, 1, None, None, 2]), expected=2)


if __name__ == "__main__":
    unittest.main()
