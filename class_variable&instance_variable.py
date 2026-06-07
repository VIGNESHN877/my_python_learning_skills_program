# class Varible and Instance variable


class Father:
    age=0

    def __init__(self):
        name="Father"  # Instance Variable 
        print("Father Contructor ! ")

Father1=Father()

Father2=Father()

print(Father1.age)
print(Father2.age)
Father1.age=20
print(Father1.age)
print(Father2.age)

# Quiz 

class car :
    wheels =4 
    def __init__(self,brand):
        self.brand=brand

car1=car("Toyota")
car2=car("Honda")


print(car1.wheels)
print(car2.wheels)
        