class Solution(object):
    def twoSum(self, nums, target):
        num_to_idx = {}
        for index, elem in enumerate(nums):
            diff = target - elem
            if diff in num_to_idx:
                return [index, num_to_idx[diff]]
            num_to_idx[elem] = index
    def containsDuplicate(self, nums):
        numbers = set()
        for elem in numbers:
            if elem in numbers:
                return True
            numbers.add(elem)
        return False


nums_1 = [1, 2, 3, 4]


solution = Solution()


print(solution.twoSum(nums_1, 5))
# assert solution.containsDuplicate(nums_1)
