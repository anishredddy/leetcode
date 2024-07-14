class Solution:
    def survivedRobotsHealths(
self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        #collision cases
        # L L , R R -no
        # L R- no
        # R L-yes
        index_map={p:i for i,p in enumerate(positions)}

        positions.sort()

        stack=[]
        for p in positions:
            i=index_map[p]

            if directions[i]=="R":
                stack.append(i)
            else:
                while stack and directions[stack[-1]]=="R" and healths[i]:
                    j=stack.pop()

                    if healths[i]>healths[j]:
                        healths[j]=0
                        healths[i]-=1
                    elif healths[i]<healths[j]:
                        healths[i]=0
                        healths[j]-=1
                        stack.append(j)
                    else:
                        healths[i]=0
                        healths[j]=0
                if healths[i]:
                    stack.append(i)
        return [h for h in healths if h>0]