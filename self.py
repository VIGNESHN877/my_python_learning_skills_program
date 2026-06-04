class car:
    def __init__(self,no_of_weels,no_of_airbages,mileages):
        print("this is a constructor")
        self.no_of_weels=no_of_weels
        self.no_of_airbages=no_of_airbages
        self.mileages=mileages

    def moveforword(self,speed):
        print("car is moving with a speed of ",speed)

    def movebackword(self):
        print("car is moving backword ! ")


car1=car(4,5,120)

print("\n","your car mileages is :",car1.mileages,"\n","your car no of weels :",car1.no_of_weels,"\n","your car no of airrbages :",car1.no_of_airbages)


        



    
