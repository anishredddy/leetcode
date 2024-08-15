class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=defaultdict(int)
        #5 - 0
        #10 - 5
        #20 - 5 , 5 ,5 or 10 , 5
        for bill in bills:
            print(bill)
            change[bill]+=1
            print(change)
            if bill==10:
                if change[5]>=1:
                    change[5]-=1
                else:
                    return False
            if bill==20:
                if change[10]>=1 and change[5]>=1:
                    change[10]-=1
                    change[5]-=1
                elif change[5]>=3:
                    change[5]-=3
                else:
                    return False
        return True