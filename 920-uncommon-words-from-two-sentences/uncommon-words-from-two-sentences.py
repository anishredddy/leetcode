class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq=defaultdict(int)
        for word in s1.split():
            freq[word]+=1
        for word in s2.split():
            freq[word]+=1
        res=[]
        for key,value in freq.items():
            if value==1:
                res.append(key)
        return res