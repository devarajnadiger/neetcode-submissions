class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()
        for num in nums:
            if num not in duplicate_set:
                duplicate_set.add(num)
            else:
                return True
        return False