from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, nums: List[int], target: int) -> List[int]:
        # numMap = {i: v for i, v in enumerate(nums)}
        arrLen = len(nums)
        for i in range(arrLen):
            for j in range(i + 1, arrLen):
                if (nums[i] + nums[j]) == target:
                    if i > j:
                        return [j, i]
                    else:
                        return [i, j]


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_1(self):
        self.e(args=dict(nums=[3, 4, 5, 6], target=7), expected=[0, 1])

    def test_2(self):
        self.e(args=dict(nums=[4, 5, 6], target=10), expected=[0, 2])

    def test_3(self):
        self.e(args=dict(nums=[5, 5], target=10), expected=[0, 1])


if __name__ == "__main__":
    unittest.main()

# optimal
# store val index hashmap
# key 0 is the solution
# store results in dict
# check if solution is in map as 0 or check if value needed is in prev map
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}  # val -> index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
