
''' 1) Print last character of each word in a string.
    2) Print first and last chararcter of each word in a string
    3) Reversing each word of the given string except the first and last char of each word
    4) Remove the first and last character of each word in a string
    5) Capitalize first and last character of each word in a string
    6) Print the string after the specified character has occurred given no. of times.
    7) 
    '''


# https://www.geeksforgeeks.org/print-last-character-of-each-word-in-a-string/?ref=rp


class StringManipulation:

    # Print last character of each word in a string
    def printLastChar(self, string):

        # by splitting each word and stroring it in a list
        lst = string.split(" ")
        print("printing last char by splitting each word : ", end=" ")
        for i in lst:
            print(i[-1], end=" ")
        print()

        # by differentiating a word with a space
        string = string + " "
        print("printing last char by diffrentiating a word with a space : ", end=" ")
        for i in range(len(string)):
            if string[i] == " ":
                print(string[i-1], end=" ")
        print()


# -----------------------------------------------------------------------------------------------------
    # print first and last chararcter of each word in string
    def printFirstLastChar(self, string):
        print("printing first and last char of each word : ", end=" ")
        for i in range(len(string)):
            if i == 0 or i == len(string) - 1:
                print(string[i], end=" ")
            if string[i] == " ":
                print(string[i-1] + " " + string[i+1], end=" ")

        print()

        # by splitting each word and storing it in a list
        lst = string.split(" ")
        print("printing last and first char by fetching each word from list : ", end=" ")
        for i in lst:
            print(i[0] + " " + i[-1], end=" ")

        print()


# ------------------------------------------------------------------------------------------------------
    # reversing each word of the given string except the first and last char of each word

    def reverseWord(self, string):
        reversedString = ""
        lst = string.split(" ")
        print("Reversing each word for the string except first and last : ", end=" ")
        for word in lst:
            ch = [h for h in word]
            i = 1
            j = len(ch) - 2
            while i < j:
                tempi = ch[i]
                ch[i] = ch[j]
                ch[j] = tempi
                i += 1
                j -= 1
            reversedString = "".join(ch)
            print(reversedString, end=" ")
        print()


# ------------------------------------------------------------------------------------------------------
    # Remove the first and last character of each word in a string

    def removeFirstLastChar(self, string):
        lst = string.split()
        updatedString = ""
        for word in lst:
            updatedString += word[1:len(word)-1] + " "
        print("String after removing first and last char of each word: ",
              updatedString, end=" ")
        print()


# -----------------------------------------------------------------------------------------------------
    # Capitalize first and last character of each word in a string

    def capitalizeFirstLastChar(self, string):
        lst = string.split()
        newString = ""

        print("string after capitalizing first and last char of each word : ", end=" ")
        for word in lst:
            ch = list(word)
            start = 0
            end = len(word) - 1
            for al in range(len(ch)):
                if (ord(ch[start]) >= 97 and ord(ch[start]) <= 122):
                    ch[start] = chr(ord(ch[start]) - 32)
                else:
                    ch[start] = ch[start]
                if (ord(ch[end]) >= 97 and ord(ch[end]) <= 122):
                    ch[end] = chr(ord(ch[end]) - 32)
                else:
                    ch[end] = ch[end]
            newString = "".join(ch)
            print(newString, end=" ")
        print()


# -----------------------------------------------------------------------------------------------------
    # Print the string after the specified character has occurred given no. of times

    def printStringAfterCondition(self, string, ch, count):
        print("string after the specified character has occurred given no. of times : ", end=" ")
        occ = 0
        if count == 0:
            print(string)
        else:
            for i in range(len(string)):
                if string[i] == ch:
                    occ += 1
                if occ == count:
                    print(string[i + 1:len(string)],end=" ")
                    break



# ------------------------------------------------------------------------------------------------------
str = "my name is abhay kumar singh"
strObj = StringManipulation()

strObj.printLastChar(str)
strObj.printFirstLastChar(str)
strObj.reverseWord(str)
strObj.removeFirstLastChar(str)
strObj.capitalizeFirstLastChar(str)
strObj.printStringAfterCondition(str, 'a', 2)

