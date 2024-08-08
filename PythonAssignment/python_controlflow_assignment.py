# Basic If-Else Statements:
# 1. Write a Python program to check if a given number is positive or negative.
num=12
if num>0:
    print("Given number is positive")  #<--output
else:
    print("Given number is negative")

# 2. Create a program that determines if a person is eligible to vote based on their age
# age=int(input("enter the value"))   #input-->45
age=8
if age>=18:
    print("Person is eligible to vote")   #<--output
else:    
    print("Person is not eligible to vote")

# 3. Develop a program to find the maximum of two numbers using if-else statements
# num1=int(input("enter the number"))   #input-->2
# num2=int(input("enter the number"))   #input-->4
num1,num2=2,4
if num1>num2:
    print(f"The maximum number is {num1}")
else:    
    print(f"The maximum number is {num2}")  #<--output
    
# 4. Write a Python script to classify a given year as a leap year or not.
year=2024
if year%4==0:
    print("Given year is a leap year")  #<---output
else:
    print("Given year is not a leap year")   
    
#5. Create a program that checks whether a character is a vowel or a consonant.
char='b'
vowel='aeiou'
if char in vowel:
    print("A character is a vowel")  
else:
    print("A character is a consonant")   #<--output
    
#6. Implement a program to determine whether a given number is even or odd.
num3=7
if num3%2==0:
    print("Given number is even") 
else:    
    print("Given number is odd") #<--output
    
#7. Write a Python function to calculate the absolute value of a number without using the `abs()` function
def absolute(n):
    if n>0:
        return n
    else:
        return -n
n=-5
print(absolute(n))    #output-->5

# 8. Develop a program that determines the largest of three given numbers using if-else statements

number=23
number1=50
number2=13
if number>number1 and number>number2:
    print(f"The largest number {number} is among three")
    if number1>number and number1>number2:
        print(f"The largest number {number1} is among three")
    # output-->The largest number 50 is among three
else:
    print(f"The largest number {number2} is among three")
        
#9. Create a program that checks if a given string is a palindrome.
def checkPalindrome(string):
    return string==string[::-1]
string="racecar"
if checkPalindrome(string):
    print("Given string is a palindrome")
else:    
    print("Given string is not a palindrome")
  
# 10. Write a Python program to calculate the grade based on a student's score.
score=int(input("enter the score"))
if score >= 90:
    grade = 'A'
else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 70:
            grade = 'C'
        else:
            if score >= 60:
                grade = 'D'
            else:
                grade = 'F'

print(f"The student's grade is: {grade}")
           
# Nested If-Else Statements
#  11. Write a program to find the largest among three numbers using nested if-else statements
number3=23
number4=50
number5=13
if number>number1 and number>number2:
    print(f"The largest number {number} is among three")
else:
    if number1>number and number1>number2:
        print(f"The largest number {number1} is among three")
    # output-->The largest number 50 is among three
    else:
        print(f"The largest number {number2} is among three")
    