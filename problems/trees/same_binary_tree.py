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

    def run(self, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        def depthSearch(p: TreeNode, q: TreeNode) -> int:

            if not p or not q:
                return (q.val if q else q) == (p.val if p else p)

            if p.val != q.val:
                return False
            return depthSearch(p.left, q.left) and depthSearch(p.right, q.right)

        return depthSearch(p, q)


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def test_long_branch(self):
        self.e(
            args=dict(
                p=TreeNode.listToTree([1, 2, 3]), q=TreeNode.listToTree([1, 2, 3])
            ),
            expected=True,
        )

    def test_symmetric(self):
        self.e(
            args=dict(
                p=TreeNode.listToTree([4, 7]), q=TreeNode.listToTree([4, None, 7])
            ),
            expected=False,
        )

    def test_inverted(self):
        self.e(
            args=dict(
                p=TreeNode.listToTree([1, 2, 3]), q=TreeNode.listToTree([1, 3, 2])
            ),
            expected=False,
        )


if __name__ == "__main__":
    unittest.main()
