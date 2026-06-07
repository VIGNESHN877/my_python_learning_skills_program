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

"""

Explation 
 
* ABC --> used to create abstract class 
* @abstractmethod --> Method must be Implemented in the child class 
* Dog inherts Aniamls and defines Sound()

why use abstrection ?

Advantages :

* Hides Complex Implemention 
* Improve is security 
* makes code easier to maintain 

Example without abstraction !

you expose all internal logic.



Example with Abstraction :

You expose only necassany functions Simple Definition :

Abstraction Means hiding Internal Implementation Details and Showing only Important 
Functionality to the user.
"""




class car(ABC):
    @abstractmethod 
    def moveforward(self):
        pass 
    def Fm(self):
        pass

class swift(car):
    def moveforward(self):
        print("swift is moving Forword !")

    def movebackward(self):
        print("swift is moving backword ! ")

    def Fm(self):
        print("swift FM playing")


class innaval(car):
    def moveforward(self):
        print("innava is moving forward ! ")
    
    def movebackword(self):
        print("Innava is moving Backwork !")

    def fm(self):
        print("Innava is playing FM !")


