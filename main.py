class Solution(object):
    def twoSum(self, nums, target):
        dicts = {}
        for i in range(0, len(nums)):
            dicts[nums[i]] = i
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in dicts and dicts[diff] != i:
                return [i, dicts[diff]]


nums_1 = [1, 2, 3, 4]


solution = Solution()


print(solution.twoSum(nums_1, 5))
