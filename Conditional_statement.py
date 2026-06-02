#COndition_Statement 
"""
if (5==5):
    print('5 is equal to 5')
    print("program successful !")
    print("Done !")
"""


def one():
    a =int(input())
    b=int(input())
    if(a==b):

        print('a is equal to 5')
        print()
        print('Program Sucessful !')
        print()
        print("Done !")
        print()
    elif (a<=b):
        print('a is b')

    else:
        print('a is not equal to 5')
        print()
        print('Done !')


def two():

    num=int(input("Enter the Number: "))

    if(0<num):
        print("This is possitive Number :",num)
    elif(0>num):
        print("This is Negaitive :",num)
    else:
        print("This is a Zero Number :",num)


#two()

def three():
    x=int(input("This is a X value :"))
    y=int(input("This is a Y value :"))
    
    if x > y :
        largest =x
    else:
        largest=y
        print("This largest Number is : ",largest)


#three()

"""a=int(input())

if(a>1):
    print('a is one')
    if(a==5):
        print("a is five")
    elif(a<100):
        print("This is  a ",a," value")
    elif(a>100):
        print("This is  a Value :",a)
    else:
        print("this is a not equal 5")

"""
'''age=int(input("Enter Your :"))
eat_pizza=False 
exercise=True '''

"""if(age <30): # 0 to 30

    if eat_pizza:
        print("unfit")
    else:  #fit31
        print("fit")
else:
    if(exercise):
        print("fit")
    else:

        print("unfit")

        """

#TERNRRY OPEARATOR 

"""print("CHILD" if(age<18) else "ADULT")

print(("unfit" if(eat_pizza) else "fit")if(age<30) else("fit" if(exercise) else"unfit") )


"""

def mass():
    income=int(input("Enter Your a income :"))
    age5=int(input("Enter Your age :"))

    if(age5<18):
        massage="your are to0 young to work ! "
        print(massage,())
    elif(age5>=18 and age5<=25 ):
        if(income<=30000):
            massage="You are Eligible for a Student Discount."
            print(massage,())
        else:
            massage="You are Eligible for a Regular Discount."
            print(massage,())
    else:
        massage="You are Not Eligible for a Regular Discount."
        print(massage)


#odd are even

"""def odd():

    number=int(input("Enter a Number :"))

    if(number%2==0):
       print("Even Number :",number)
    else:
        print("Odd NUmber :",number)

odd()"""
number21=int(input("Enter a Number :"))
print("Even Number :" if(number21%2==0) else"Odd Number :",number21) 