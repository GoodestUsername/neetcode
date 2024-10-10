from collections import defaultdict
from typing import List
import unittest


class Solution:
    """First Attempt"""

    # def run(self, nums: List[int], k: int) -> List[int]:
    #     numsDict = defaultdict(int)
    #     for num in nums:
    #         numsDict[num] += 1

    #     return [
    #         i[0] for i in sorted(numsDict.items(), key=lambda x: x[1], reverse=True)
    #     ][:k]
    def run(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        for num in nums:
            numsDict[num] += 1

        frequencies = [[] for i in range(len(nums) + 1)]
        for num, occurrences in numsDict.items():
            frequencies[occurrences].append(num)

        solution = []

        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_1(self):
        self.e(args=dict(nums=[1, 2, 2, 3, 3, 3], k=2), expected=[3, 2])

    def test_2(self):
        self.e(args=dict(nums=[7, 7], k=1), expected=[7])

    def test_3(self):
        self.e(args=dict(nums=[1, 2], k=2), expected=[1, 2])


if __name__ == "__main__":
    unittest.main()
