class Solution:
    def place(self,words,space):
        
        if len(words)==1:
            s=words[0]
            s+=" "*space
            return s

        gap=space//(len(words)-1)
        rem=space%(len(words)-1)

        s=""
        for i in range(len(words)-1):
            s+=words[i]+" "*gap
            if rem:
                rem-=1
                s+=" "
        s+=words[-1]
        return s

    def place_last(self,words,space):
        if len(words)==1:
            s=words[0]
            s+=" "*space
            return s
        space-=len(words)-1
        s=" ".join(words)
        s+=" "*space
        return s


    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        curr_sum=0
        curr_s=[]
        for word in words:
            if curr_sum+len(word)==maxWidth:
                curr_s.append(word)
                spaces=len(curr_s)-1
                res.append(self.place(curr_s,spaces))

                #reset
                curr_s=[]
                curr_sum=0
                continue
            elif curr_sum+len(word)>maxWidth:
                spaces=maxWidth-(curr_sum-len(curr_s))
                res.append(self.place(curr_s,spaces))

                #reset
                curr_s=[]
                curr_sum=0
            curr_s.append(word)
            curr_sum+=len(word)+1
            # print(curr_s)
        if curr_sum:
            spaces=maxWidth-(curr_sum-len(curr_s))
            res.append(self.place_last(curr_s,spaces))
        return res