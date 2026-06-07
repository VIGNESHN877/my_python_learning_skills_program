#Two Different Class 

#  method overredding 
class Father:
    def say_hello(self):   
        print("hello from father ! ")

class child(Father):
    def say_hello(self):
        super().say_hello()
        print("Hello from Child ! ")


child=child()
child.say_hello()