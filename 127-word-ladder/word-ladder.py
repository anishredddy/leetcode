from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei=defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                nei[pattern].append(word)

        visited=set()
        visited.add(beginWord)
        q=deque()
        q.append(beginWord)

        res=1

        while q:

            for j in range(len(q)):
                word=q.popleft()

                if endWord==word:
                    return res
                for i in range(len(word)):
                    pattern=word[:i]+"*"+word[i+1:]
                    for w in nei[pattern]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            res+=1

        return 0