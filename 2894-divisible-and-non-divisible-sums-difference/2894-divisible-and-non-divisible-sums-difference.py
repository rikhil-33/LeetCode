class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num3 = ((n*(n+1))//2)
        k = n//m
        num2 = m * (k*(k+1)//2)
        num1 = num3 - num2
        return (num1 - num2)