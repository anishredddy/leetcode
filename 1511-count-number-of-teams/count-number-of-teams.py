class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res=0
        for i in range(1,len(rating)-1):

            left_count_1=0
            left_count_2=0
            for j in range(0,i):
                if rating[j]<rating[i]:
                    left_count_1+=1
                if rating[j]>rating[i]:
                    left_count_2+=1
            right_count_1=0
            right_count_2=0
            for k in range(i+1,len(rating)):
                if rating[k]>rating[i]:
                    right_count_1+=1
                if rating[k]<rating[i]:
                    right_count_2+=1
            res+=left_count_1*right_count_1+left_count_2*right_count_2
            
        return res
                
