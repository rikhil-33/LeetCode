class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        for i in nums:
            if i == 0:
                return 0
            elif i<0:
                neg_count += 1
            
        if (neg_count % 2 == 0):
            return(1)
        elif (neg_count % 2 != 0):
            return(-1)
        else:
            return(0)
