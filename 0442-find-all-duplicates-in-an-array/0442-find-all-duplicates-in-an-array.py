class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = []
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                d.append(nums[i])
            else:
                s.add(nums[i])
        return d