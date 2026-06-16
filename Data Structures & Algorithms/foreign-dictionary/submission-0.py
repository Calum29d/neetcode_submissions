
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))

            #if first word is greater than the word infront and same prefix then its invalid ordering
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    #the char in word1 comes before the char in word2 in the alphabet
                    adj[word1[j]].add(word2[j])
                    break
        
        visit = {} #False = visited, True = current path were on
        res = []

        #post order topological sort
        def dfs(c):
            if c in visit:
                #if True is returned then we found a cycle so its invalid
                return visit[c]
            
            visit[c] = True
            for neighbor in adj[c]:
                #if cycle is found then return True 
                if dfs(neighbor):
                    return True
            
            #no longer in the current path
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
                



        