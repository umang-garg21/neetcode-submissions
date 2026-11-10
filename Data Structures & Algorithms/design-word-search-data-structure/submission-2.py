class TrieNode:
    def __init__(self):
        self.children= {}
        self.endofword= False

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()

    def addWord(self, word: str) -> None:
        cur= self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
        
            cur=cur.children[c]
        cur.endofword= True

    def search(self, word: str) -> bool:

        cur= self.root
        #print("cur children", cur.children)
        def dfs(cur, string):
            
            for i, c in enumerate(string):
                
                if c!= '.':
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
                else:
                    #print("char", c)
                    #print("current children:", list(cur.children))
                    if not cur.children:
                        return False
                    
                    for child in cur.children.values():
                        if dfs(child, string[i+1:]):
                            return True
                    return False

            return cur.endofword 

        return dfs(cur, word)
