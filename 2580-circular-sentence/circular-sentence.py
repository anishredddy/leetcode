class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split()
        if words[0][0]!=words[-1][-1]:
            # print("f")
            return False
        prev=words[0][-1]
        for i in range(1,len(words)):
            if words[i][0]!=prev:
                return False
            prev=words[i][-1]
        return True