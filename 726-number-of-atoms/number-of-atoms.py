class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[]
        i=0
        while i<len(formula):
            if formula[i]==")":
                count=""
                while i+1<len(formula) and formula[i+1].isnumeric():
                    count+=formula[i+1]
                    i+=1
                if count=="":
                    count=1
                else:
                    count=int(count)
                #now get string from stack
                s=""
                while stack:
                    char=stack.pop()
                    if char=="(":
                        break
                    s=char+s

                stack.append(s*count)
            else:
                stack.append(formula[i])
            i+=1
        
        formula="".join(stack)
        d=defaultdict(int)

        i=count=0
        
        while i<len(formula):
            if formula[i].isupper():
                ele=formula[i]
                if i+1<len(formula) and formula[i+1].islower():
                    i+=1
                    ele+=formula[i]
                count=""
                while i+1<len(formula) and formula[i+1].isnumeric():
                    count+=formula[i+1]
                    i+=1

                if count=="":
                    count=1
                else:
                    count=int(count)
                d[ele]+=count
            i+=1
        res=""
        for key in sorted(d.keys()):
            res+=key
            if d[key]!=1:
                res+=str(d[key])
        return res