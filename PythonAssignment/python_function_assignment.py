# Basics of Functions:
# 1.Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.
def calculateSum(num1,num2):
    return num1+num2
print("The sum of the two number ",calculateSum(2,5))  #output-->7

# 2. Create a Python function that takes two arguments and returns their product.
def productOfTwoNum(num1,num2):
    return num1*num2
print(productOfTwoNum(2,4))   #output-->8


# Function Parameters and Arguments:
# 1.Write a Python program that defines a function with default argument values.
def sums(a=9,b=10):
    return a+b
print(sums())   #output-->19

# 2.Create a Python function that accepts a variable number of arguments and calculates their sum.
def variableNoArgumentSum(*arg):
    sums=0
    for i in arg:
        sums+=i    
    return sums
print(variableNoArgumentSum(1,2,3,4,5,6))     #output-->21

# Return Values and Scoping:
# 1.Write a Python program that demonstrates the use of global variables within functions.
counter=0
def increment():
    global counter
    counter+=1
    print("The increment value of the counter is ",counter)
 
def decrement():
    global counter
    counter-=1
    print("The decrement value of the counter is ",counter) 

increment()   #output-->1
decrement()   ##output-->0

#2.Create a Python function that calculates the factorial of a number and returns it.
def calculFact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(calculFact(6))  #output-->720     

#3.How can you access variables defined outside a function from within the function?
number=2
def accessVariable():
    # accessing global varibale
    print("Variable inside the function ",number)   #output-->2
accessVariable()   
def modifyVariable():
    global number
    number+=1
    print("The modifying value of global variable is ",number)  #output-->3
modifyVariable()
print("Value of x outside the function after modification:", number)  #output-->3      

# Lambda Functions and Higher-Order Functions:
# 1.Write a Python program that uses lambda functions to sort a list of tuples based on the second element.
tupleList=[(3,2),(2,1),(1,5),(4,3),(2,6),(6,4)]
sortListOfTuples=sorted(tupleList,key=lambda x:x[1])
print(sortListOfTuples)  #output-->[(2, 1), (3, 2), (4, 3), (6, 4), (1, 5), (2, 6)]

# 2.Explain the concept of higher-order functions in Python, and provide an example.
def operations(operation,x,y):   #taking argument three parameter
    return operation(x,y)     #first parameter is use to function
def add(x,y):
    return x+y
def mul(x,y):
    return x*y

result1=operations(add,2,4)
result2=operations(mul,2,4)
print("The sums is ",result1)   #output-->The sums is  6
print("The product is ",result2)   #output-->The product is 8

# 3.Create a Python function that takes a list of numbers and a function as arguments, applying the function to each element in the list.

def applyEach(elements, func):
    return [func(element) for element in elements]

numbers = [1, 2, 3, 4, 5]

# Define a function to be applied
def square(x):
    return x ** 2

# Apply the function to each element in the list
squared_numbers = applyEach(numbers, square)

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



# function using for loop
# 1.Write a Python program to print numbers from 1 to 10 using a for loop.
def num_print():
    for i in range(1,11):
        print(i,end=" ")
        
num_print()  #output--> 1 2 3 4 5 6 7 8 9 10 

# 2.Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop.
def sumOfAllNumbers():
    sums=0
    for j in range(1,101):
        sums+=j
    return sums
print(sumOfAllNumbers())  #output-->5050

# 3.How do you iterate through a list using a for loop in Python?
def iterateList(lst):
    for k in lst:
        print(k,end=" ")  #output-->a s d f g 
       
lst=['a','s','d','f','g'] 
iterateList(lst)  

# 4.Write a Python program to find the product of all elements in a list using a for loop.
def productOfAllElements(lists):
    product=1
    for i in lists:
        product*=i
        
    return product
lists=[1,2,3,4,5]            
print(productOfAllElements(lists))   #output-->120

# 5.Create a Python program that prints all even numbers from 1 to 20 using a for loop.
def printsAllEvenNumbers():
    for i in range(1,21):
        if i%2==0:
            print(i,end=" ")
                          
printsAllEvenNumbers()    #output-->2 4 6 8 10 12 14 16 18 20

# 6.Write a Python program that calculates the factorial of a number using a for loop.

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))  #output--->120

# 7.How can you iterate through the characters of a string using a for loop in Python?

def iterateString(strings):
    for k in strings:
        print(k,end=" ")  
strings="helloworld"
iterateString(strings)  #output-->h e l l o w o r l d 

# 8.Write a Python program to find the largest number in a list using a for loop.
def largestNumber(lst):
    maxi=0
    for i in lst:
        if i>maxi:
            maxi=i
    return maxi  
lsts=[1,45,-67,0,34,90,78]
print(largestNumber(lsts))  #output-->90

# 9.Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop

def fibonacciSequence(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
specifiedLimit=8    
fibonacciSequence(specifiedLimit)     #output-->0 1 1 2 3 5 8 13

# 10. Write a Python program to count the number of vowels in a given string using a for loop.
def countNoVowels(strs):
    vowels='aeiou'
    counts=0
    for i in strs:
        if i in vowels:
            counts+=1
            
    return counts

strings1="duplicates"
print(countNoVowels(strings1))    #output-->4    

# 11.Create a Python program that generates a multiplication table for a given number using a for loop

def multiTable(num):
    for k in range(1,11):
        print(num*k,end=" ")
        
num=5
multiTable(num)  #output-->5 10 15 20 25 30 35 40 45 50 

# 12.Write a Python program to reverse a list using a for loop.
def reverseList(lst):
    reverseList=[]
    for i in range(len(lst)-1,-1,-1):
        reverseList.append(lst[i])
    return reverseList    
lst1=[10,20,30,40]
print(reverseList(lst1))  #output-->[40, 30, 20, 10]

# 13.Write a Python program to find the common elements between two lists using a for loop.
def commonElement(list1,list2):
    commonList=[]
    for i in list1:
        for j in list2:
            if i==j:
                commonList.append(j)
    return commonList
            
list1=[1,2,3,4,5,6]
list2=[7,8,3,9,5]
print(commonElement(list1,list2))  #output--> [3,5]

# 14.write a program for loop to iterate through the keys and values of a dictionary in Python.
def iterateKeysValues(dicts):
    for i in dicts:
        print(i,dicts[i])
        
dicts={"name":"Alice","age":23,"gender":"male","city":"Canda"}        

iterateKeysValues(dicts)
# name Alice
# age 23
# gender male
# city Canda

#15. Create a Python program that checks if a string is a palindrome using a for loop.
def is_palindrome(s):
    s = s.lower()  # Normalize the string to lowercase
    length = len(s)   #7
    
    # Compare characters from the start and end of the string
    for i in range(length):
        if s[i] != s[length - 1 - i]:    #1st iteration s[0] 'r' == s[7-1-0]==s[6] 'r'
            return False
        # Stop checking once we reach the middle
        if i >= length // 2:
            break
    
    return True

test_string = "Racecar"
print(f'"{test_string}" is a palindrome.' if is_palindrome(test_string) else f'"{test_string}" is not a palindrome.')

# 16.Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.
def sumAllOddNumbers():
    sums=0
    for h in range(1,51):
        if h %2 !=0:
            sums+=h
    return sums

print(sumAllOddNumbers())     #output->>625   

# 17.Create a Python program that counts the number of words in a sentence using a for loop
def countWordsSentence(sentence):
    words=sentence.split()
    counts=0
    for i in words:
        counts+=1
    return counts
sentence="program that counts the number" 
print(countWordsSentence(sentence))    #output-->5

# 18.Write a Python program that checks if a given year is a leap year using a for loop.
def checkLeapYear(years):
    for k in range(years,years+1):
        if (k%4==0 and k%100!=0) or k%400==0:
            return True
        
    return False
years=2025  
print(checkLeapYear(years)) #output-->false


 
   
        
        