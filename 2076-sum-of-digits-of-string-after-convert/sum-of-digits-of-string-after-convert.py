class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new_s=""
        for char in s:
            new_s+=str(ord(char)-ord('a')+1)
        
        while k>0:
            char_sum=0
            for char in new_s:
                char_sum+=int(char)
            new_s=str(char_sum)
            k-=1
        return char_sum