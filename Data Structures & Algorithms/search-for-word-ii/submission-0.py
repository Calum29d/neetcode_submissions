class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordIndex = -1

    def addWord(self, word, index):
        cur = self
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        cur.wordIndex = index
            
#I could definetly think about how to solve the problem but coding it is really difficult
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i, w in enumerate(words):
            root.addWord(w, i)

        rows, cols = len(board), len(board[0])
        visit = set()
        res = []

        def dfs(r, c, node):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or
                (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            
            if node.endOfWord:
                res.append(words[node.wordIndex])
                node.endOfWord = False
            
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res
