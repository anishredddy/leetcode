class Solution:
    def countWinningSequences(self, s: str) -> int:
        # fire > earth
        # water> fire
        # earth > water
        # same no point

        # given alice creatures
        # never summon same creature in 2 successive rounds

        #if bob has to win
        # he should have 1 win more than loss
        # n losses , minimum n+1 wins, remaining draws
        # res=0

        MOD=10**9 + 7

        chars=["F","W","E"]

        @cache
        def dfs(i,char,score):
            # nonlocal res
            if i==len(s) and score>0:
                return 1
            if i==len(s) and score<=0:
                return 0
            res=0
            for ch in chars:
                if ch!=char:
                    if ch=="F" and s[i]=="E":
                        res+=dfs(i+1,"F",score+1)%MOD
                    elif ch=="W" and s[i]=="F":
                        res+=dfs(i+1,"W",score+1)%MOD
                    elif ch=="E" and s[i]=="W":
                        res+=dfs(i+1,"E",score+1)%MOD
                    elif ch==s[i]:
                        res+=dfs(i+1,ch,score)%MOD
                    elif ch=="E" and s[i]=="F":
                        res+=dfs(i+1,"E",score-1)%MOD
                    elif ch=="F" and s[i]=="W":
                        res+=dfs(i+1,"F",score-1)%MOD
                    elif ch=="W" and s[i]=="E":
                        res+=dfs(i+1,"W",score-1)%MOD
            return res%MOD
        
        return dfs(0,"",0)
            