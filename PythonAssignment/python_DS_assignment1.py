# 1. Create a list with integers from 1 to 10.
lists=[1,2,3,4,5,6,7,8,9,10]

# 2. Find the length of a list without using the `len()` function.
def length(lists):
    length=0
    for i in lists[0:]:
        length+=1
    return length

lists=[1,2,3,4,5,6,7,8,9,10]
print(length(lists))   #output-->10

# 3. Append an element to the end of a list.
def appendList(list1,Element):
    
    list1.append(Element)
    return list1
list1=[1,2,3,4,5]
element=6
print(appendList(list1,element))   #output-->[1,2,3,4,5,6]

# 4. Insert an element at a specific index in a list
def insertElement(list2,element2):
    list2.insert(4,element2)
    return list2
list2=[1,2,3,4,5,6]
element2=56
print(insertElement(list2,element2))   #output-->[1, 2, 3, 4, 56, 5, 6]

# 5. Remove an element from a list by its value.
def removeElement(list3,element3):
    list3.remove(element3)
    return list3
list3=[1,2,3,4,5]
element3=3
print(removeElement(list3,element3))  #output-->[1, 2, 4, 5]

# 6. Remove an element from a list by its index.

def removeIndexElement(lists):
    lists.pop(3)
    return lists
lists=[33,4,56,39,90]
print(removeIndexElement(lists))    #output-->[33, 4, 56, 90]


# 7. Check if an element exists in a list.
def checkElementExist(list4,element4):
    for i in list4[0:]:  #travser upto len of list
        if i==element4:
            return True
    return False    
list4=[1,2,34,6,73,22]   
element4=34
if checkElementExist(list4,element4):
    print("Element exists in lists")   #output-->Element exists in lists
else:    
    print("Element not exists in lists")   


#8. Find the index of the first occurrence of an element in a list.
def  indexFirstOccurrence(list5,element5):
    firstOccu=list5.index(element5)
    return firstOccu
    
myList = [10, 20, 30, 20, 10]
element = 20

index =indexFirstOccurrence(myList,element)

print("The index of the first occurrence of", element, "is", index)
# output-->The index of the first occurrence of 20 is 1

# 9. Count the occurrences of an element in a list
def  countOccurrences(list5,element5):
    firstOccu=list5.count(element5)
    return firstOccu
    
myList = [10, 20, 30, 20, 10,20,20]
element = 20

index =countOccurrences(myList,element)

print("The index of the first occurrence of", element, "is", index)
# output-->The index of the first occurrence of 20 is 4

# 10. Reverse the order of elements in a list
def reverseOrderElements(lists):
    reverse=sorted(lists,reverse=True)
    return reverse
myLists=[10,20,30,40,50]
print(reverseOrderElements(myLists))  #output-->[50, 40, 30, 20, 10]