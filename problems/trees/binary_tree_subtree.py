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
    def run(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root and not subRoot:
            return True

        def depthSearch(p: TreeNode, q: TreeNode) -> int:
            if not p and not q:
                return

            if (not p and q) or (p and not q):
                return False

            if (
                (p and p.left or p.right)
                and (not q.left and not q.right)
                and p.val != q.val
            ):
                return False

            if p.val == q.val:
                if not p.left and not p.right and not q.left and not q.right:
                    return True
                l = True
                r = True
                if p.left and q.left:
                    l = depthSearch(p.left, q.left)
                elif (p.left and not q.left) or (not p.left and q.left):
                    l = False
                if p.right and q.right:
                    r = depthSearch(p.right, q.right)
                elif (p.right and not q.right) or (not p.right and q.right):
                    r = False
                head = l and r
                if head:
                    return head

            return depthSearch(p.left, q) or depthSearch(p.right, q)

        return depthSearch(root, subRoot)


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
                root=TreeNode.listToTree([1, 2, 3, 4, 5]),
                subRoot=TreeNode.listToTree([2, 4, 5]),
            ),
            expected=True,
        )

    def test_subroot_not_subtree(self):
        self.e(
            args=dict(
                root=TreeNode.listToTree([1, 2, 3, 4, 5, None, None, 6]),
                subRoot=TreeNode.listToTree([2, 4, 5]),
            ),
            expected=False,
        )

    def test_min_repeat_node(self):
        self.e(
            args=dict(
                root=TreeNode.listToTree([1, 1]),
                subRoot=TreeNode.listToTree([1]),
            ),
            expected=True,
        )

    def test_false_middle(self):
        self.e(
            args=dict(
                root=TreeNode.listToTree([3, 4, 5, 1, None, 2]),
                subRoot=TreeNode.listToTree([3, 1, 2]),
            ),
            expected=False,
        )

    def test_null_guards(self):
        self.e(
            args=dict(
                root=TreeNode.listToTree(
                    [
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        None,
                        1,
                        2,
                    ]
                ),
                subRoot=TreeNode.listToTree(
                    [1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]
                ),
            ),
            expected=True,
        )


if __name__ == "__main__":
    unittest.main()


# brute force dfs
# class Solution:

#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True
#         if not root:
#             return False

#         if self.sameTree(root, subRoot):
#             return True
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#     def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not root and not subRoot:
#             return True
#         if root and subRoot and root.val == subRoot.val:
#             return self.sameTree(root.left, subRoot.left) and self.sameTree(
#                 root.right, subRoot.right
#             )
#         return False

# serialization and pattern matching
# class Solution:
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         if root == None:
#             return "$#"

#         return (
#             "$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)
#         )

#     def z_function(self, s: str) -> list:
#         z = [0] * len(s)
#         l, r, n = 0, 0, len(s)
#         for i in range(1, n):
#             if i <= r:
#                 z[i] = min(r - i + 1, z[i - l])
#             while i + z[i] < n and s[z[i]] == s[i + z[i]]:
#                 z[i] += 1
#             if i + z[i] - 1 > r:
#                 l, r = i, i + z[i] - 1
#         return z

#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         serialized_root = self.serialize(root)
#         serialized_subRoot = self.serialize(subRoot)
#         combined = serialized_subRoot + "|" + serialized_root

#         z_values = self.z_function(combined)
#         sub_len = len(serialized_subRoot)

#         for i in range(sub_len + 1, len(combined)):
#             if z_values[i] == sub_len:
#                 return True
#         return False
