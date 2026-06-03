"""


def area_of_retangle(length,weith): # this is a paramenters in the function (length,weith)==> positional Argument 
   
    area=length*weith
    return area

length=int(input("Enter the area of Length :")) #this function calculates the area of the retangle
weith=int(input("Enter the area of weith :")) # input value of the weith and length
#function output argumnet of the value 
retangle_area=area_of_retangle(length,weith) #pasitional Argument (frist value, secoud value)
print(retangle_area)"""



 #1.Position (order)

 # In the Position value are passed based on the their poisition (order) in their function cells 

"""name=input("Enter Your Name : ")
age=input("Enter your age :")
 #Example :
def student(name,age):
      print("Name:",name)
      print("age:",age)


student(name,age)"""

#this  is a positional argument its used for a parameter on the value and assign to the value in the print statement of the value 


# Explanation
#vignesh ===> goes to name 
#21 ==>goes to age 
"""

#keyword  Argument :


# Value are passed using Paremeter Name :

#Example :
def student(name,age):
    print("Name:",name)
    print("Age :", age)

    
student(age="21",name="Vignesh N")
    """
# Explanation  in the code is keys values calling to the paramenters 

#Order Does not Matter Because name are specified 


# Defult Argument 

# function Parameters Have Defult value. 
# If no values is provided , in the -python user the defult

#Example :
"""
def greet(name="Guest"): # this a dewfult value is a Guest in the python program 
    print("Hello",name) # this is print statement and add for a parameter funtion statement 


greet()   # print for a greet function a statement  there are print for a Defult Name function of the Vlaue 
greet("Vignesh N") # this line callege for a updated for a new line of the function in the statement \
greet("Dinesh Kumar S") # exmple 2 : this line callege for a updated for a new line of the function in the statement """


#Combined Example :

"""
1.Positional Argument 
2.Keyword Argument 
3.Defult Argument 

there are is three type of Argument combined in the program in the code that name callege is a Combined Argument 
"""

def employee(name,age="21",city="salem"):
    print("Name :",name)
    print("Age :",age)
    print("city :",city)

employee("Baskar")
print()
employee("VIgnesh N","22","Chinnasalem")
print()
employee(name="Dinesh",age=21,city="malliyakari")
