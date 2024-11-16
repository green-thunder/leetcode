class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        division = {}
        for i, num in enumerate(nums):
            if target - num in division:
                return [division[target - num], i]
            division[num] = i

        return []


twoSum = Solution().twoSum

nums = [1,2,4,5,6,7,8,9,10,12,41]
target = 51

result = twoSum(nums, target)

print(result)