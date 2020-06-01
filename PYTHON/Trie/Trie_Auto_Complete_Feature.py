



# --------*----- Alternate method to insert word in trie -------*---------

class TrieNode:
    def __init__(self,data):
        self.data = data
        self.isEndOfWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('*')
        self.word_list = []

    def insertData(self,word):
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode(letter)
            temp = temp.children[letter]
        
        temp.isEndOfWord = True


# ------------------ Removing a word from trie structure -----------------
# removing a word from Trie means nothing but setting its isEndOfWord to False.

    def deleteData(self,word):
        if word == "":
            return True
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        temp.isEndOfWord = False

        return temp.isEndOfWord

    def searchWord(self,word):
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]

        return True if temp.isEndOfWord else False

# --------*-----Auto-complete feature using Trie.-------*---------

    def suggestionsRec(self, node, word): 
          
        # Method to recursively traverse the trie 
        # and return a whole word.  
        if node.isEndOfWord: 
            self.word_list.append(word) 
  
        for a,n in node.children.items(): 
            self.suggestionsRec(n, word + a) 
  
    def printAutoSuggestions(self, key): 
          
        # Returns all the words in the trie whose common 
        # prefix is the given key thus listing out all  
        # the suggestions for autocomplete. 
        node = self.root 
        not_found = False
        temp_word = '' 
  
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
  
            temp_word += a 
            node = node.children[a] 
  
        if not_found: 
            return 0
        elif node.isEndOfWord and not node.children: 
            return -1
  
        self.suggestionsRec(node, temp_word) 
  
        for s in self.word_list: 
            print(s,end=" ") 
        return


# ------------------ Testing the Trie Tree Structure -----------------
t = Trie()
strings = [
    'sin',
    'singh',
    'sign',
    'sinus',
    'sit',
    'silly',
    'side',
    'son',
    'soda',
    'sauce',
    'sand',
    'soap',
    'sar',
    'solo',
    'sour',
    'sun',
    'sure',
    'an',
    'ant',
    'aunt',
    'hell',
    'hello',
    'help',
    'helps',
    'hellish',
    ]
for key in strings:
    t.insertData(key)

print("is word Found in the String : ",t.searchWord('thier'))

print("Words matched with the pattern are : ",end=" ")
t.printAutoSuggestions('he')

print(t.deleteData("help"))
t.printAutoSuggestions('he')

