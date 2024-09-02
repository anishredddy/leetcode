class TrieNode:
    def __init__(self):
        self.children={}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()   

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        q = deque([(curr, 0)])
        
        while q:
            currNode, index = q.popleft()
            if index == len(word):
                if currNode.word:
                    return True
                continue

            char = word[index]
            if char == '.':
                for childChar, childNode in currNode.children.items():
                    q.append((childNode, index + 1))
            elif char in currNode.children:
                q.append((currNode.children[char], index + 1))
        
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)