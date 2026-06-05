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