class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in twoSum:
                return [twoSum[diff], index]
            twoSum[number] = index