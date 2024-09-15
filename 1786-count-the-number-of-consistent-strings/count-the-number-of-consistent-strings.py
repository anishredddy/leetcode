class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bit_mask=0
        for c in allowed:
            bit=1<<(ord(c)-ord('a'))
            bit_mask|=bit
        res=len(words)
        for word in words:
            for c in word:
                bit=1<<(ord(c)-ord('a'))
                if bit&bit_mask==0:
                    res-=1
                    break
        return res