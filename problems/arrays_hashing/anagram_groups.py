from typing import Dict, List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, strs: List[str]) -> List[List[str]]:
        solutionDict: Dict[str, List[str]] = dict()
        for c_str in strs:
            sorted_str = "".join(sorted(list(c_str)))
            if sorted_str in solutionDict:
                solutionDict[sorted_str].append(c_str)
            else:
                solutionDict[sorted_str] = [c_str]

        # real solution doesn't require sorting this final output
        # can just do solutionDict.values()
        return sorted([sorted(sol) for sol in solutionDict.values()])


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_1(self):
        self.e(
            args=["act", "pots", "tops", "cat", "stop", "hat"],
            expected=sorted(
                [["hat"], sorted(["act", "cat"]), sorted(["stop", "pots", "tops"])]
            ),
        )

    def test_2(self):
        self.e(
            args=["x"],
            expected=[["x"]],
        )

    def test_3(self):
        self.e(
            args=[""],
            expected=[[""]],
        )


if __name__ == "__main__":
    unittest.main()


""" optimal
create a hash key based off the anagram in numerical instead of sorting the strings


EG: anagram is [3, 0, 0, 0, 0, 0, 0, 1, ..., 1, 1, ..., 1, ...0]

complexity
original
Time complexity: O(m*nlogn)
Space complexity: O(m*n)
vs
optimal
Time complexity: O(m*n)
Space complexity: O(m)

"""


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             res[tuple(count)].append(s)
#         return res.values()
