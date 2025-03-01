from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dicts = Counter(nums)
        sorted_dicts = sorted(dicts.keys(), key=lambda x: dicts[x], reverse=True)
        return sorted_dicts[:k]


settings = Solution()

nums = [-9, -2, -3, -3]
k = 2

print(settings.topKFrequent(nums, k))
