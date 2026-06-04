# object Oriented Program 

no_of_wheels=4
mileage=20.9
no_of_airbages=5


def moveforword():
    print("Car is Moving !")
      

def movebackword():
    print("Car is moving backword ! ")


# copy of the number of templete so that called for a class

#  That are created for a called of the class that name insantest 

# class is a template
#object   is a class copy


movebackword()
moveforword()


class car:
    no_of_wheels =0
    mileage=0.0
    no_of_airbages=0

    def moveforward(self):
        print("car is moving !")

    def movebackword(self):
        print("Car is moving backward !")

car1=car() # instance of the case :object instantion
print(car1.mileage)
car2=car()
print("millage :",car2.mileage)
car2.mileage=25.0
print("milleage :",car2.mileage)
car3=car()
print(car1.mileage)
car3=car()
car3.moveforward()

car1.mileage=25
car1.no_of_airbages=8
car1.no_of_wheels=8



car2=car()
car2.mileage=22
car2.no_of_airbages=8
car2.no_of_wheels=8

print("\n","This is your car mileage :",car2.mileage,"\n","this is your car airbages : ",car2.no_of_airbages,"\n","this is your car wheels :",car2.no_of_wheels)
print("\n","This is your car mileage :",car1.mileage,"\n","this is your car airbages : ",car1.no_of_airbages,"\n","this is your car wheels :",car1.no_of_wheels)

