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
def remove_whitespace(s):
    return s.replace(" ","")

string="Hello world "
print(remove_whitespace(string))  #output-->Helloworld

#8. Find the length of a string without using the len() function
string="Hello,world"
length=0
for i in string:
    length+=1
print("length of a string is :" ,length)
# output-->length of a string is : 11

# 9. Check if a string contains a specific word.
def contain_word(string,speci_word):
    return speci_word in string

string="Hello world, welcome to Python."
speci_word="welcome"

if contain_word(string,speci_word):
    print(f"The word '{speci_word}' is present in the string")
else:
    print(f"The word '{speci_word}' is not present in the string")
    #output --> The word 'welcome' is present in the string

# 10. Replace a word in a string with another word.
str7="Hello , Python!"
str7.replace("Python","Java")
# output-->'Hello , Java!' 
