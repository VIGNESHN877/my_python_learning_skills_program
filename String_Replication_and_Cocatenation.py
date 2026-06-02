"""stars="*"*20
greeting= " happy" + " Holidays !"
print(stars,greeting,stars,sep="\n")


#input From user 

#Average of Mark :
def Mark():
    Mark1=float(input("Enter the Tamil Mark :"))
    Mark2=float(input("Enter the English Mark :"))
    Mark3=float(input("Enter the Maths Mark :"))
    Mark4=float(input("Enter the Basic Electrical Engineering(T) Mark :"))
    Mark5=float(input("Enter the Computer Technology Mark :"))
    Mark6=float(input("Enter the Basic Electrical Engineering(P) :"))

    
    total_Mark=Mark1+Mark2+Mark3+Mark4+Mark5+Mark6

    print("\n","This your Tamil Mark: ",Mark1,
        "\n","This your English Mark:",Mark2,
        "\n","This  the Maths Mark :",Mark3,
        "\n","This  the Basic Electrical Engineering(T) Mark :",Mark4,
        "\n","This the Computer Technology Mark :",Mark5,
        "\n","This the Basic Electrical Engineering(P) :",Mark6)
    print()

    print("This is Your 12th Total Marks :",total_Mark)

    total_Mark= total_Mark/6
    print("out of 600 Marks :",total_Mark)

    print(
        "\n","This  the Maths Mark :",Mark3,
        "\n","This  the Basic Electrical Engineering(T) Mark :",Mark4,
        
        "\n","This the Basic Electrical Engineering(P) :",Mark6)

    total_Cut_off=Mark4+Mark6

    total_Cut_off=total_Cut_off/2
    print()
    print("this is your BEE(T),BEE(P) Total Mark of cutoff :",total_Cut_off)
    print()
    total_Cut_off=total_Cut_off+Mark3
    print("This Your Engineering Cutoff Mark :",total_Cut_off)



a = 2
b = 3
c = 4


result=3**a+ 2*b*c + 2**c
print(result)

a = 2
b = 3
c = 4
#3a^2+b-2c
result1=(3*a**2+b-(2*c))
print(result1)
print()

#unit Digit

num =(input())
num=num.split(",")
print(len(num))

print(len(num)-1),print(num*2)
"""
#Tenth Digit 
#11859
num1=int(input(100))
num1=num1/10
print(num1)