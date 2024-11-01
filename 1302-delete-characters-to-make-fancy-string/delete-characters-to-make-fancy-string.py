class Solution:
    def makeFancyString(self, s: str) -> str:
        new_s=""
        for i in range(len(s)-2):
            if s[i]==s[i+1] and s[i]==s[i+2]:
                continue
            new_s+=s[i]
        return new_s+s[len(s)-2:]