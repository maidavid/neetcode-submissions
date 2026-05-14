class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:\

        result = {}

        for i in range(len(nums)):
            result[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result and result[diff] != i:
                return [i, result[diff]]
        return []


                


