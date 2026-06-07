
# OOPS 

"""
Polmorphism in python is an object-Oriented Programming(OOP) concept that mean "Many form"

Its allows the same method or function name to perform Different actions Depending on the Object.

types of Polymorphism in python

1. Method Overiding (Runtime Polgmophism) Child Class Changes The Behavior of a Parent Class Method 
"""

#program

"""class Animal:  #parent class
    def sound(self):
        print("Animal mokes Sound")

class Dog(Animal): #child 1 
    def sound(self):
        print("Dog barks")

class cat(Animal):  # child 2
    def sound(self):
        print("cat means")

d = Dog()
e=cat()

d.sound()
e.sound()

# Here Sound() behaves Different for Different objects

"""

# 2. Opertor Polymorphism

#same Opertor works Different for Different Data  Types.
"""
print(5+3) # addition 

print("Hi"+" All") # string conate notion


# Works Differently for Integers and strings


# Function Polymorphism 

# Built - in FUnctions work with Multiple data Types

# Example :

print(len("Python"))
print(len(1,2,3,4))
"""

#len () works with strings and lists Real - life Examples

"""
Think of a remote control butten :

Press power Button on TV --> TV turn CN
Press Power Button on AC --> AC turn ON
Same action (Power)--> Different Dehavior

This () Polymophism

Simple Definition

polymorphism Means one method or Function Can Have Multiple Behaviors Depending on the 
Object or Data Type.


"""
class car :
    def moveforword(self): # this line of argument is function print for function value 
        print("Moving")

    def moveforword(self,speed): # this class function 
        print(speed)

def sum(a,b,c=21): # this line a value function
        return a+b+c
    
    
print(sum(21,43,56)) # print for a function 

def sum(*args):
     ans=1
     for i in args:
          ans+=i
          return ans

summation=sum(1,2)
print(summation) 

"""
class Car:

    def moveforword(self, speed):
        print(speed)

def sum_numbers(*args):

    ans = 0

    for i in args:
        ans += i

    return ans

summation = sum_numbers(1, 2)

print(summation)

"""