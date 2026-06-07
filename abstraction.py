from abc import ABC, abstractmethod
"""
Abstraction in python is an object- Oriendted Program (OOP) Concept use dto hide Implementation 
details and show only for essential feature to the users.


In simple Words 

The user Knows What an object does,but not how it works internally.


Real - life Example :

Think about an ATM Machine :
You Know :
 * withdraw Money 
 * Check Balance 
 * Deposit Money 

 you do not know the internal Proessing Of the bank System.
 This is Abstraction.

 Abstraction in python using Abstract Class 

 Python Provides the abc Module (Abstract Base Class ) To Create Abstraction

 Exxample :

          Python form inpart ABC, abstractmethod 

# Abstract Class
 
"""

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# chid class 

class Dog(Animal):
    def sound(self):
        print("Dog Barks ! ")


object=Dog()
object.sound()


