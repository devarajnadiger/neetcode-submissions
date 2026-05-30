class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i, num in enumerate(nums):
            differnce = target - num
            if differnce in val_index:
                return [val_index[differnce],i]
            val_index[num] = i
