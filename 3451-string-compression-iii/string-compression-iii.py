class Solution:
    def compressedString(self, word: str) -> str:
        if word=="":
            return ""
        comp=""
        pre=word[0]
        count=1
        for char in word[1:]:
            if pre!=char:
                comp+=str(count)+pre
                pre=char
                count=1
            else:
                count+=1
                if count==10:
                    comp+="9"+pre
                    count=1
        comp+=str(count)+pre
        return comp