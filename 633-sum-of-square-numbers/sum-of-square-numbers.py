class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(sqrt(c))

        while left<=right:
            current_sum=left*left+right*right
            if current_sum<c:
                left+=1
            elif current_sum>c:
                right-=1
            else:
                return True
        return False
