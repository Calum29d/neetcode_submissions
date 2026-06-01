#class for the trie node
class TrieNode:
    def __init__(self):
        self.children = {} #holds the children of the current trie node
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True #cur is now at the end of the word so update the flag


    def search(self, word: str) -> bool:

        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord #return the flag, true if it is the end of a word
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True #only returns true if the prefix is part of the tree
        
        