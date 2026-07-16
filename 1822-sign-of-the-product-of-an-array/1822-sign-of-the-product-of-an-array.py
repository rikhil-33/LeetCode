class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = math.prod(nums)
        if 0 in nums:
            return(0)
        elif (product>0):
            return(1)
        else:
            return(-1)