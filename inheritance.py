#parent class


class Animal:
   def  sound(self):  # this is a parent class 
            print("Animal make a sound")


class dog(Animal):
    def bark(self): # this is a child class
        print("Dog bark")


object=dog()
object.sound()
object.bark()


#i exptced output is : animal makes sound , Dog bark