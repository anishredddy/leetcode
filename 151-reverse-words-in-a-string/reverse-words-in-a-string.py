class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        stack=[]

        curr_s=""
        prev=""

        for char in s:
            if char==" ":
                if prev==" ":
                    continue
                else:
                    stack.append(curr_s)
                    curr_s=""
            else:
                curr_s+=char
            prev=char
        if curr_s!="":
            stack.append(curr_s)
        return " ".join(stack[::-1])