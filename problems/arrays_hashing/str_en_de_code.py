from typing import List
import unittest


class Solution:
    def encode(self, strs: List[str]) -> str:
        return ""

    def decode(self, s: str) -> List[str]:
        return [""]

    def run(self, args, de_en):
        if de_en == "de":
            return self.decode(args)
        else:
            return self.encode(args)


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_dup(self):
        self.e(args=["neet", "code", "love", "you"], expected=True)


if __name__ == "__main__":
    unittest.main()
