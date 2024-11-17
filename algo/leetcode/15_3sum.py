# Three Sum
# https://leetcode.com/problems/3sum/description/
# Difficulty: Medium
# 17.03.2024

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 Pointers solutioin
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = set()
    #     sorted_nums = sorted(nums)
    #     for i_id, i in enumerate(sorted_nums):
    #         for j_id, j in enumerate(sorted_nums[i_id+1:]):
    #             lower_b = (i_id + j_id + 2)
    #             k_pos = lower_b + (len(sorted_nums) - lower_b) // 2
    #             print("Lower_b", lower_b, k_pos, len(sorted_nums) - lower_b)
    #             while len(sorted_nums) - k_pos > 0 and k_pos - lower_b > 0:
    #                 print("i", i, "j", j, "k", sorted_nums[k_pos], "k_pos", k_pos)
    #                 if i + j + sorted_nums[k_pos] == 0:
    #                     res = ":".join(sorted(i, j, sorted_nums[k_pos]))
    #                     print("Res: ", res)
    #                     result.add(res)
    #                 if len(sorted_nums) - k_pos == 1 or k_pos - lower_b == 1:
    #                     break
    #                 if sorted_nums[k_pos] < -i-j:
    #                     k_pos += (len(sorted_nums) - k_pos) // 2
    #                 else:
    #                     k_pos -= (len(sorted_nums) - k_pos) // 2

    #     res = []
    #     print(result)
    #     for str_res in result:
    #         r = [int(i) for i in str_res.split(':')]
    #         res.append(r)
    #     return res

    # def _sum3_in_list(self, sum3: List[int], nums: List[List[int]]) -> bool:
    #     for num in nums:
    #         if set(num) == set(sum3):
    #             return True
    #     return False

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     # Brute Force
    #     result = []
    #     for i_id, i in enumerate(nums):
    #         for j_id, j in enumerate(nums[i_id+1:]):
    #             for k in nums[i_id+j_id+2:]:
    #                 if i+j+k == 0:
    #                     sum3 = [i, j, k]
    #                     if not self._sum3_in_list(sum3, result):
    #                         result.append(sum3)

    #     return result


def main():
    try:
        assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
        assert Solution().threeSum([]) == []
        assert Solution().threeSum([0]) == []
        assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
        print("Passed all test cases!")
    except AssertionError:
        print("Failed test cases! Please, debug!")


if __name__ == "__main__":
    main()
