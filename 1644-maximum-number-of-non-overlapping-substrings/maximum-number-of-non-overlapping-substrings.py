class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ranges={}

        for ind,ch in enumerate(s):
            if ch not in ranges:
                ranges[ch]=[]
            ranges[ch].append(ind)

        # here index of occurance of every lettter is present

        #intuition

        #if we want it to be non-overlapping substring + all occurances of a letter

        #the substring should be left occur<length<right occurance 

        # keep checking for global min and global max

        visited=set()
        res=[]

        for r in ranges:
            left,right=ranges[r][0],ranges[r][-1]
            templ,tempr=left,right

            while True:
                for ch in set(s[templ:tempr]):
                    templ=min(templ,ranges[ch][0])
                    tempr=max(tempr,ranges[ch][-1])
                if (templ,tempr)==(left,right):
                    break
                left,right=templ,tempr
            ranges[r]=(templ,tempr)

        #found left and right

        sorted_ranges=sorted(ranges.values(),key=lambda pair:pair[1])
        print(sorted_ranges)
        print(ranges)

        prev=0

        for start,end in sorted_ranges:
            if start>=prev:
                res.append(s[start:end+1])
                prev=end
        return res