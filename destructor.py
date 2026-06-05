#Desstructor 


"""
def__def__(self):
   print("This is a Destructor ! ")

   def__def__(self):
   print("This is a Destruetor !",self)

   def__def__(self):
   print("This is a Destnutor !"id=(self))
"""

class car:
    def __init__(self,car_name,no_of_wheels,no_of_airbage,mileage,):
        self.no_of_wheels = no_of_wheels 
        self.no_of_airbage= no_of_airbage
        self.mileage = mileage
        self.car_name =car_name

    def __del__(self):
      print("This is a Destructor ! ")

    def moveforword(self,speed):
       print("car is moving with a speed of ",speed)

    def movebackword(self):
       print("car is moving backword ")


car1=car("swift",4,5,80)
print(car1.mileage,"\n",car1.no_of_wheels,"\n",car1.no_of_airbage,"\n",car1.moveforword(22),car1.movebackword)