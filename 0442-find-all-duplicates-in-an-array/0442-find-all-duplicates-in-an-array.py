class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicates.append(nums[i])
            else:
                seen.add(nums[i])
        return duplicates