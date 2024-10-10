from typing import List
import unittest


class Solution:
    # first attempt
    # def run(self, nums: List[int]) -> List[int]:
    #     output = [0] * len(nums)

    #     zero_indexes = []
    #     final_product = 1

    #     for i, num in enumerate(nums):
    #         if num == 0:
    #             zero_indexes.append(i)
    #         else:
    #             final_product *= num

    #     return output

    def run(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        products = []
        final_product = 1
        temp_product = 1

        for i, num in enumerate(nums):
            products.append(final_product)
            final_product *= num

        for i in range(len(nums) - 1, -1, -1):
            output[i] = temp_product * products[i]
            temp_product *= nums[i]

        return output


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    # def test_has_zero(self):
    #     self.e(args=[-1, 0, 1, 2, 3], expected=[0, -6, 0, 0, 0])

    def test_all_zero(self):
        self.e(args=[0, 0], expected=[0, 0])

    # def test_non_zero(self):
    #     self.e(args=[1, 2, 4, 6], expected=[48, 24, 12, 8])


if __name__ == "__main__":
    unittest.main()
