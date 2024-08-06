# String
# 1. Write a program to reverse a string.
str="condition"
result=str[::-1]
print(result)   #output --> noitidnoc

# 2. Check if a string is a palindrome.
str1="racecar"
result1 = str1[::-1]
if(str1 == result1):
    print("This is palindrome string")
else:
    print("This is not palindrome string")  #output -->This is palindrome string

# 3. Convert a string to uppercase.
str3="condition"
str3.upper() # output--> 'CONDITION'

# 4. Convert a string to lowercase.
str4="CONDITION"
str4.lower()  #output--> 'condition'

# 5. Count the number of vowels in a string.
str5="programming"
vowels="aeiouAEIOU"
count=0
for char in str5:
    if char in vowels:
        count+=1
print("the number of vowels in a string are : ",count)
# output--> the number of vowels in a string are :  3

# 6. Count the number of consonants in a string.
str6="programming"
consonants= "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count=0
for char in str6:
    if char in consonants:
        count+=1
print("the number of consonants in a string are : ",count)        
# output-->the number of consonants in a string are :  8

# 7. Remove all whitespaces from a string.
def removeWhitespace(s):
    return s.replace(" ","")

string="Hello world "
print(removeWhitespace(string))  #output-->Helloworld

#8. Find the length of a string without using the len() function
string="Hello,world"
length=0
for i in string:
    length+=1
print("length of a string is :" ,length)
# output-->length of a string is : 11

# 9. Check if a string contains a specific word.
def containWord(string,speciWord):
    return speciWord in string

string="Hello world, welcome to Python."
speciWord="welcome"

if containWord(string,speciWord):
    print(f"The word '{speciWord}' is present in the string")
else:
    print(f"The word '{speciWord}' is not present in the string")
    #output --> The word 'welcome' is present in the string

# 10. Replace a word in a string with another word.
str7="Hello , Python!"
str7.replace("Python","Java")
# output-->'Hello , Java!'

# 11. Count the occurrences of a word in a string.
def occurrencesWord(text,word):
    if word in text:
        return text.count(word)
text="Python is easy to learn. Python is powerful and versatile."    
word="Python"

print(occurrencesWord(text,word))  #output-->2

# 12. Find the first occurrence of a word in a string.
def occurrencesFirstWord(texts,words):
    if words in texts:
        return texts.find(words)
    else:
        return -1
text="Python is easy to learn. Python is powerful and versatile."    
word="Python"

print(occurrencesFirstWord(text,word))  #output-->0

# 13. Find the last occurrence of a word in a string.
def occurrencesLastWord(text1,word1):
    if word1 in text1:
        return text1.rindex(word1)
    else: 
        return -1
text1="Python is easy to learn. Python is powerful and versatile."    
word1="Python"

print(occurrencesLastWord(text1,word1))  #output-->25

# 14. Split a string into a list of words
def splitString(string):
    return string.split()
string="Python is powerful and versatile."
print(splitString(string))   #output-->['Python', 'is', 'powerful', 'and', 'versatile.']

# 15. Join a list of words into a string.
def wordsIntoString(lists,str):
    return  str.join(lists)
lists=["aa","ab","bb"]
string=" "
print(wordsIntoString(lists,string))   #output-->aa ab bb

# 16. Convert a string where words are separated by spaces to one where words
# are separated by underscores.
def separatedBySpaces(text2):
    return text2.replace(" ","_")

text2="Words are separated by spaces"
print(separatedBySpaces(text2))  #output-->Words_are_separated_by_spaces

# 17. Check if a string starts with a specific word or phrase
def stringStartsWith(str2,specifiWord):
    return str2.startswith(specifiWord)

str2="Python is easy to learn. Python is powerful and versatile."
specifiWord="Python"
if stringStartsWith(str2,specifiWord):
    print(f"string is starts with a {specifiWord}")
else:    
    print(f"string is not starts with a {specifiWord}")   #output--> string is starts with a Python

# 18. Check if a string ends with a specific word or phrase
def stringEndsWith(str3,specifiWord1):
    return str3.startswith(specifiWord1)

str3="Python is easy to learn. Python is powerful and versatile."
specifiWord1="Python"
if stringEndsWith(str2,specifiWord):
    print(f"string is end with a {specifiWord}")
else:    
    print(f"string is not end with a {specifiWord}")   #output-->string is end with a Python

# 19. Convert a string to title case (e.g., "hello world" to "Hello World")
def stringToTitle(str3):
    return str3.title()

str3="my name is harshada chaudhari"
print(stringToTitle(str3))   #output--> My Name Is Harshada Chaudhari

# 20. Find the longest word in a string.
def findLongestWord(sentence):
    words=sentence.split()
    longestWord=""
    for word in words:
        if len(word)>len(longestWord):
            longestWord=word
    return longestWord    

sentence = "The quick browns fox jumps over the lazy dog"
print("The longest word is:", findLongestWord(sentence))   #output-->browns

