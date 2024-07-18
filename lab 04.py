# This file contains several incomplete function definitions with stub
# values. Lab04_tests.py have tests to check if the functions are correct.
# Your assignment is to complete each function according to the
# functions' descriptions.
#
# Once you complete a function, use pytest on the test functions
# in lab04_tests.py to see if your functions are working correctly


#1

def notStringContainingR(word):
    if type(word)==str:
        for letter in word:
            if letter != 'r' or letter !='R':
                return True
    if type(word)!=str or str(word)=="":
        return True
     
    '''
    - Return True when word is a string that contains no letter 'r' (or 'R')
    - It should work both for lower and upper case.
    - When word isn't a string or is an empty string (""), return True
    (because it is not a string contaning an R).
    - You can check if the word value is a string with type(word) == str 
    '''
    
    

#2

def hasVowel(word):
    
    if type(word)==str:
        for letter in word:
             if letter in "aeiouAEIOU":
                 return True
            
    return False
                


    '''
    - Return True when word is a string that contains a vowel
    (a,e,i,o,u,A,E,I,O,U).
    - It should work for both lower and upper case vowels.
    - When word doesn't have a vowel, return False. Return True otherwise.
    - If word isn't a string, return False (because it is not a string
    containing a vowel).
    - Hint: recall the boolean operator "in" and use that when
    checking if a character is a vowel.
    '''
  
    


#3

def isNumber(item):
    if type(item)==int or type(item)==float:
        return True
    return False
    '''
    - Return True if item is of type int or type float, otherwise return
    False.
    - You can check if item is an int with type(item) == int, and a float
    with type(item) == float
    '''

   
#4

def onlyContainsStrings(theList):
    if theList ==[]:
        return False
    if type(theList)!=list:
        return False
    for item in theList:
        if type(item)==str:
            return True
        return False
        
    '''
    - Returns True if theList is a list containing only strings.
    - The parameter theList can be anything.
    - An empty list should return False since it doesn't contain a string.
    - If theList is not a list type, return False since theList is not a list
    containing only strings.
    - Note: you can check if theList is a list with type(theList) == list
    '''
    

    
    

#5

def contains(x, theList):
    if type(theList)!=list or theList ==[]:
        return False
    for item in theList:
        if item == x:
            return True
        return False
        

    '''
    - Returns True if the value of x is in theList.
    - The parameters x and theList can be anything.
    - An emptyList should return False since it doesn't contain any values
    (including x).
    - If theList is not a list type, return False since x is not in a list.
    '''
    

#6

def abbreviate(word):
    if type(word)!=str:
        return ("")
    if type(word) ==str:
        return(word[0:3])
    
    
    '''
    - Returns a string with (up to) the first three characters of
    the string word.
    - The value of word can be anything.
    - If word is not a string, return an empty string ("").
    '''


    


#7

def hasMultiplesOf(x, listOfNums):
    
    '''
    - Returns True if ALL items in listOfNums are multiples of x.
    
    - theList can have elements of any type.
    
    - If listOfNums is not a list type, return False.
    
    - If listOfNums is empty, return False since no items are a multiple
    of x
    
    - If listOfNums contains an element that is not a number (int or
    float), return False.
    '''
    
        
   




#8

def countEvens(listOfInts):
    evens = 0 

    if type(listOfInts)!=list:
        return 0
    for number in listOfInts:
        if type(number)==float or type(number)==int:
            if number%2==0:
                evens+=1 
    return evens
        
    



    
    '''
    - Returns an integer value representing the number of even numbers that
    exist in listOfInts.
    - Return 0 if listOfInts is not a list type or if no even number exists
    in listOfInts.
    - Note: elements in listOfInts can contain any data type.
    '''
    















#9

def computeGrade(percentage):
    if type(percentage)==float:
        percentage = int(percentage)
    if type(percentage)==int:
        if percentage in range(90, 101):
            return ('A')
        if percentage in range(80,90):
            return ('B')
        if percentage in range(70, 80):
            return ('C')
        if percentage in range(60,70):
            return ('D')
        if percentage in range(0,60):
            return ('F')
    return ("")
    

#10

# Definition of a Book namedtuple object used for the
# following function below.
from collections import namedtuple
Book = namedtuple("Book", "title author price")

def expensiveBooks(price, listOfBooks):
    if (type(price)==int or type(price)==float) and (type(listOfBooks)==list):
        newlist = []
        for item in listOfBooks:
            if item.price >=price:
                newlist.append(item.title)
        return newlist
    return [] 
                
                
        
    



    
   
