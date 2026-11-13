class TrieNode:
    def __init__(self):
        self.children={} # hashmap
        self.endofword= False

class Worddict:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur= cur.children[c]
        cur.endofword=True
        #print("self.endofword=True")

    def prefix_search(self, prefix):

        cur= self.root
        for c in prefix:
            if c not in cur.children:
                return False, False
            cur= cur.children[c]

        if cur.endofword:
            #print("End of word reached")
            return True, True
        else:
            #print("Here")
            return True, False
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = set()
        dirs = {(-1,0), (0, -1), (1,0), (0,1)}

        # construct the trie
        word_dict= Worddict()
        # add words to the trie dictionary 
        for word in words:
            word_dict.insert(word)


        def prefix_in_grid(pre_str, i,j, visited):
            nonlocal res
            pre_str= pre_str+ board[i][j]

           # print("prestring", pre_str)
            new_visited= visited.copy()
            new_visited.add((i,j))

            # does my dict still has pre_Str
            got_words, found_word= word_dict.prefix_search(pre_str)
            if found_word:
                res.add(pre_str)
            
            if got_words:
                for dx, dy in dirs:
                    posx, posy = i+dx, j+dy
                    if 0<= posx< len(board) and 0<= posy < len(board[0]) and (posx, posy) not in new_visited:
                        prefix_in_grid(pre_str, posx, posy, new_visited)
                    else:
                        continue

            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited= set()
                prefix_in_grid("", i,j, visited)
        

        return list(res)


                

        

        



         
        
        



            
