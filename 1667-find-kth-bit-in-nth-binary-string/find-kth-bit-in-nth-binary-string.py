class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findK(si,i):
            rev=""
            for char in si:
                if char=="1":
                    rev+="0"
                else:
                    rev+="1"
            sii=si+"1"+rev[::-1]
            if i+1==n:
                return sii
            return findK(sii,i+1)
        if n==1:
            return "0"
        return findK("0",1)[k-1]