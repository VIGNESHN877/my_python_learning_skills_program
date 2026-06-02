"""#for loop statement 


for i in range(0,100,2):
    print(i)

for j in range(0,100,2):
    print(j)

for i in range(5,11,2):
    print(i,end="\n")


num1=5

while(num1>0):
    print('code io')

    num1-1


for i in range(51-1):
    print(i)

num2=5

for i in range(10,50): #fist value is a starting value and next value is ending value 
    print(i)

#loop incresment value 
num3=5

for i in range(0,-100,-2):#fist value is a starting value and next value is ending value and steping value
    print(i)

for i in range(5,11,2):
    print(i)"""



# this end a FOR A LOOP FUNCTION OF THE VALUE IN THE FOR LOOP SYSTEM

#<--------------------- WHILE LOOP ----------------------------------------->


#WHILE(CONDITION)

#LET GO THE PROGRAMMING IN THE PYTHON ON THE SYSTEM OF THE C CODE 


"""i=1

while i <9: # 1<10 is true 
    print(i) #print i
    i=i+1   #1=+1=2"""



"""i =1
while i<10:
    print(i)
    i+=1"""
    

"""count=1

while(count<100):
    print(count)
    count+=1"""
#this is a while loop statement 

#jump Statement using if condition statement


"""for i in range(1,10,1):
    if i ==5:
       continue # this is a jump statement of the value 
    elif i ==7:
        break # This is a  break statement of the for loop on the system
    print(i)
else:
    print("enjoy a fun")"""

"""for j in range(5):
    print(j)
else:
    print("enjoy a fun")"""


"""for i in range(0,5,+1):
    for j in range(i,5):
        print("*"*2)
"""

"""for i in range(1,10):
    print(i)"""

n = int(input("Enter The Number : "))

for j in range(1,n+1):
    for i in range(1,j+1):
        print("*", end="")
    print()


for j in range(n):
    for i in range(n):
        print("*", end="")
    print()