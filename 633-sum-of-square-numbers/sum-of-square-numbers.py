class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(math.sqrt(c))

        while left<=right:
            print(left,right)
            current_sum=left*left+right*right
            if current_sum<c:
                left+=1
            elif current_sum>c:
                right-=1
            else:
                return True
        return False
