class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root=int(math.sqrt(c))
        b2=set()
        for b in range(root+1):
            b2.add(b*b)
        

        for a in range(root+1):
            if c-a*a in b2:
                return True
        return False