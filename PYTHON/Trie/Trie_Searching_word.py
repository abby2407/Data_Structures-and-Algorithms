
'''Trie is an efficient information reTrieval data structure. Using Trie, search complexities 
   can be brought to optimal limit (key length).'''

#                       root
#                    /   \    \
#                    t   a     b
#                    |   |     |
#                    h   n     y
#                    |   |  \  |
#                    e   s  y  e
#                 /  |   |
#                 i  r   w
#                 |  |   |
#                 r  e   e
#                        |
#                        r               


from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        return ord(ch) - ord('a')

    def insert(self,data):
        temp = self.root
        length = len(data)
        for key in range(length):
            index = self._charToIndex(data[key])
            if index not in temp.children:
                temp.children[index] = self.getNode()
            temp = temp.children.get(index)
        
        temp.isEndOfWord = True

    def searchData(self,data):
        temp = self.root
        length = len(data)
        for key in range(length):
            index = self._charToIndex(data[key])
            if index not in temp.children:
                return False
            temp = temp.children.get(index)
        return True if temp != None and temp.isEndOfWord else False


# ------------------ Testing the Trie Tree Structure -----------------
strings = ['the', 'a', 'thier', 'and', 'for', 'of', 'bygone']

t = Trie()
for key in strings:
    t.insert(key)

print("is given word found : ",t.searchData('and'))

