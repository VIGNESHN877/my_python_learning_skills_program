"""# object Oriented Program 

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

"""


# create the a class value in the function in the bank account 

class Bank_account():
    customer_name=input("Enter Your name : ")
    balance=float(input("this is your account balance :"))
    account_number=int(input("Enter the your account number :"))

customer3=Bank_account()
customer3.customer_name
customer3.balance
customer3.account_number

customer1=Bank_account()
customer1.customer_name="Dinesh kumar . S"
customer1.balance=145000
customer1.account_number=214406933

customer2=Bank_account()
customer2.customer_name="siva"
customer2.balance=100000.50
customer2.account_number=121210650

print("\n",customer3.customer_name,"\n",customer3.balance,"\n",customer3.account_number,"\n")
print("\n",customer1.customer_name,"\n",customer1.balance,"\n",customer1.account_number,"\n")
print("\n",customer2.customer_name,"\n",customer2.balance,"\n",customer2.account_number,"\n")


