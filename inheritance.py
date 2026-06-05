"""#parent class


class Animal:
   def  sound(self):  # this is a parent class 
            print("Animal make a sound")


class dog(Animal):
    def bark(self): # this is a child class
        print("Dog bark")


object=dog()
object.sound()
object.bark()



#i exptced output is : animal makes sound , Dog bark"""



"""
type of tnheritance in python 
1.single inhertance
once child inherits one parent 

class A :
   pass
class B:
    pass
"""

"""
2.Muliple inheritance 
once child inherits multiple parents 

class A:
    pass
class B:
    pass 
    
class(A,B):
    pass
"""

"""
3.Multiple Inheritance

class A:
    pass
class B:
    pass

class c(B):
    pass
    
"""

"""
4.Hierachial Inheritance 

Multiple child class inherit one perent 
class A:
    pass
class B(A):
    pass 
class A(B):
    pass

"""

"""
5.Hybird inheritance is a cobination of the Different inheritance types
"""
"""
class vehicle: # parent class
    no_of_wheels=4

    def moveforword(self):
        print(
            "Vehicle is moving forword !"
        )


class car(vehicle): #child class
        no_of_airbages=3

car1=car()
print(car1.no_of_airbages)
print(car1.no_of_wheels)

car1.moveforword()

#There are reused for parent class to child class """


# super is used to call parent class method .

"""class person:                       #parent class

    def __init__(self,name):       # function 
        self.name=name


class student(person):   #child class 
    def __init__(self, name,mark):  # function 
        super().__init__(name)
        self.mark=mark

object=student("vignesh N",90)
print(object.name)
print(object.mark)
"""

# here Super.__init__(name) call the parent class constructor 


# simple Definition :

# inhertance means creating a new class form an existing class and rensing its properties and methods.

"""

class vehicle : # parent class
    no_of_wheels=4


    def moveforword(self):
        print("Vehicle is moving forword !")



class car(vehicle):  # child class 
    no_of_airbages=3

car1=car()
print(car1.no_of_wheels)
print(car1.no_of_airbages)

car1.moveforword()
#There are reused for parent class to child class

class bike(vehicle): # child class 2 
    mileage=60.0

# 3) Multi - level Inheritance 

class Maruthi(car): # New class called a old child  class 
    mileage=25.0

car2=Maruthi() # class print to the child tree class calling 
print(car2.no_of_airbages)
print(car2.no_of_wheels)
print(car2.mileage)
car2.moveforword()
# there are called Multi Level Inheritance

# grand father---> Farther ---> son ]--> connect with face and body languge but Diffarent skills """


# Multiple Inheritance 


"""class father:
    hair_color="White"

class mother:
    eye_color="blue"


class child(father,mother):
    no_of_legs=2

   
child1=child()


print(child1.no_of_legs)
print(child1.hair_color)
print(child1.eye_color)"""

#damain program 

"""class car():
    no_of_airbages=3

class maruthi(car):
    mileage1=25.0

class toyato(car):
    mileage=30.0


class toythi(maruthi,toyato):
    has=touchscreen=car

car1=toythi()
print(car1.no_of_airbages)
print(car1.mileage1)
print(car1.mileage)
"""

#Quiz

class Father:
    hair_color="White"

    def music():
        print("Kuthu paatui")

class Mother:
    hair_color="Black"
    eye_color="Blue"

class Child(Father,Mother):
    no_of_legs=2
    
Child2=Child()


Child.music()


