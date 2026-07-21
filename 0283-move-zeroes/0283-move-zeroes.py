class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = []
        z = []
        for i in range(len(nums)):
            if nums[i] != 0:
                n.append(nums[i])
            else:
                z.append(nums[i])
        nums[:] = n + z
