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

name=input("Enter Your Name : ")
age=input("Enter your age :")
 #Example :
def student(name,age):
      print("Name:",name)
      print("age:",age)


student(name,age)

#this  is a positional argument its used for a parameter on the value and assign to the value in the print statement of the value 


# Explanation
#vignesh ===> goes to name 
#21 ==>goes to age 


#keywor