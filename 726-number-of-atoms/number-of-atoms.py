class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[defaultdict(int)]
        i=0

        while i<len(formula):
            if formula[i]=="(":
                stack.append(defaultdict(int))
            elif formula[i]==")":
                curr_map=stack.pop()
                count=""
                while i+1<len(formula) and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                count=1 if not count else int(count)

                for ele in curr_map:
                    curr_map[ele]*=count

                prev_map=stack[-1]
                for ele in curr_map:
                    prev_map[ele]+=curr_map[ele]


            else:
                element=formula[i]
                if i+1<len(formula) and formula[i+1].islower():
                    element=formula[i:i+2]
                    i+=1
                count=""
                while i+1<len(formula) and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                # print("count, ",count)
                count=1 if not count else int(count)

                curr_map=stack[-1]
                curr_map[element]+= count
            i+=1
        curr_map=stack.pop()

        res=""
        for ele in sorted(curr_map.keys()):
            count=curr_map[ele]
            res+=ele
            if count!=1:
                res+=str(count)
        return res