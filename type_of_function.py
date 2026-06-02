"""#in functions 

def hello():
    for i in range(100):
        print("Hello World !")


def geet():
    name=input("Enter Name :")
    print("Good Morning",name)




#Two return of Function 

#void function 
#non - void function

#no return to the value that hand void function .

#Function 

def add(a,b):
   
    return a+b
#in functions 

def hello():
    for i in range(100):
        print("Hello World !")

hello()

def geet():
    name=input("Enter Name :")
    print("Good Morning",name)

geet()

#Two return of Function 

#void function 
#non - void function

#no return to the value that hand void function .

#Function 

def add(a,b):  #add function a,b is the a,b is the value 
    return a+b  # a + b is a return value is function a+b



#print(add(12,12))



def add1(a,b):
    return a+b


def sub(a,b):
    return a-b


def Mul(a,b):
    return a*b

def div(a,b):
    return a/b

def reminder(a,b):
    return a%b

a=int(input("Enter a A of value :"))
b=int(input("Enter a B of value :"))

sum1=add1(a,b)
sum2=sub(a,b)
sum3=Mul(a,b)
sum4=div(a,b)
sum5=reminder(a,b)
print(f"\n\n",sum1,"\n\n",sum2,"\n\n",sum3,"\n\n",sum4,"\n\n",sum5)


def area_of_retangle(length,weith):

    area=length*weith
    return area
    retangle_area=area_of_retangle(34,24)
    print(area_of_retangle)
  """


# Argument or Parameters

def area_of_retangle(length,weith): # this is a paramenters in the function (length,weith)==> positional Argument 
    
    area=length*weith
    return area


length=int(input("Enter the area of Length :")) #this function calculates the area of the retangle
weith=int(input("Enter the area of weith :")) # input value of the weith and length
#function output argumnet of the value 
retangle_area=area_of_retangle(length,weith) #pasitional Argument (frist value, secoud value)



print(retangle_area)