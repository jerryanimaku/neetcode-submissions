class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in twoSum:
                return [twoSum[diff], index]

            twoSum[num] = index
            
