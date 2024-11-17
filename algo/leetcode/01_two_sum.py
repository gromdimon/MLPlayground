# Two Sum
# https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# 03.03.2024

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bruteforce
        # for idx1, num1 in enumerate(nums):
        #     for idx2, num2 in enumerate(nums):
        #         if num1 + num2 == target and idx1 != idx2:
        #             return [idx1, idx2]

        # Hashmap
        # num_to_i = {}
        # for i, num in enumerate(nums):
        #     num_to_i[num] = i
        # for i, num in enumerate(nums):
        #     if target - num in num_to_i and num_to_i[target-num] != i:
        #         return [i, num_to_i[target-num]]

        # One-loop hashmap
        num_to_i = {}
        for i, num in enumerate(nums):
            # First check, because for repeated values we will change the position in hashmap
            # and thus num_to_i[target-num] == i
            second_val = target - num
            if second_val in num_to_i and num_to_i[second_val] != i:
                return [i, num_to_i[second_val]]
            num_to_i[num] = i


def main():
    try:
        assert set(Solution().twoSum([2, 7, 11, 15], 9)) == {0, 1}
        assert set(Solution().twoSum([3, 2, 4], 6)) == {1, 2}
        assert set(Solution().twoSum([3, 3], 6)) == {0, 1}
        print("Passed all test cases!")
    except AssertionError:
        print("Failed test cases! Please, debug!")


if __name__ == "__main__":
    main()
