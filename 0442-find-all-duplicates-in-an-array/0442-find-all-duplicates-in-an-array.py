class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                dup.append(nums[i])
            else:
                seen.add(nums[i])
        return dup