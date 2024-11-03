class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s=s+s
        for i in range(len(goal)):
            if s[i:len(goal)+i]==goal:
                return True

        return False