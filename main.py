class Solution(object):
    def twoSum(self, nums, target):
        num_to_idx = {}
        for index, elem in enumerate(nums):
            diff = target - elem
            if diff in num_to_idx:
                return [index, num_to_idx[diff]]
            num_to_idx[elem] = index


nums_1 = [1, 2, 3, 4]


solution = Solution()


print(solution.twoSum(nums_1, 5))
