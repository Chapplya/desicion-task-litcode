class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        const = 1
        for inx_1 in range(len(nums)):
            for inx_2 in range(len(nums)):
                if inx_2 != inx_1:
                    const *= nums[inx_2]
            result.append(const)
            const = 1
        return result


settings = Solution()

nums = [1, 2, 4, 6]

print(settings.productExceptSelf(nums))
