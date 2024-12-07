from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimized
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        return []
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]
        # return[]


if __name__ == "__main__":
    nums = [3,2,3]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)
