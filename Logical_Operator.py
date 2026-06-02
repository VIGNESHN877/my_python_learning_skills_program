#Logical_Operator


# one Value of the true or false 
# And both are value  of True or False 


a = 5
b = 10 
print(a==5) # a= 5 but a==5 it's true value 
print(b==10) #b = 10 it's true value 
print(a==10) #a = 10 it's a false 
print(b==5) #b = 5 it's a fasle 

# or  Operator value 

print(a==10 or b==5)  # 0 + 0 = 0
print(a==5 or b==10)  # 1 + 1 = 1
print(a==5 or b==12)  # 1 + 0 = 1
print(a==10 or b==10) # 0 + 1 = 1

# AND Operator Value 

print(a==5 and b==12)   # 1 + 0 = 0
print(a==10 and b==10)  # 0 + 1 = 0
print(a==12 and a ==15) # 0 + 0 = 0
print(a==5 and b==10)   # 1 + 1 = 1

print(not(a==5)) # fasle 
print(not(a==10)) # true 
print(not(b==10)) # false 
print(not(b==12)) #true


work = "this my workout"
work1="this my workout"
print(work==work1)
print(not(work==work1))


#Find Out the quiz 
# Logical Operators 
num = 5
num1=22
print(num > 5) #> there are work to the ">" this kind of operator 
print(num <=5 ) #< there are work to the "<" this kind of operator
print(num > 10 or num < 5) #10>10 or 10=5 false
print(num < 10 or num1 > 5) #10<10 or 10>5 true
print(num%2==0 or num1%3==0) # ans 1 its false 
print(num%2==1 or num1%2==1) # ans 0 its true 

num2=10
print(num2 > 5 and num < 15) #true 
print(num2 < 5 and num2> 15) # false 
print()
print(num2 > 5 or num2 < 15) # true
print(num2 < 5 or num2 > 15) #false
print(num2 > 5 or num2 < 9) #true
print(num2 > 12 or num2 < 12) #true 
print()
print(not(num2 > 5 or num2 < 15)) # true there are ops false 
print(not(num2 < 5 or num2 > 15)) #false there are ops true
print(not(num2 > 5 or num2 < 9)) #true there are ops false
print(not(num2 > 12 or num2 < 12)) #true there are ops false


#binary system
num5=122
print(num5)
print(bin(num5))
print(int(num5))

print(bin(num5))
print(num & num5)

print(type(num))
print(type(num5))
print(num and num5)
print(bin(num5))
print(num >> num5)
print()
print(num << num5)
print(num ^ num5)
print(num | num5)
a=2
b=3
print(a>>b)
print(a<<b)
print(a>>b)

x=10
y=4
print(x&y)
print(x|y)
print(x^y)

aaa="Sorry"
print(aaa*100)

a1="Welcome to my youtube channal\t"
a2= "Mr.Vignesh pls subcrable to my channal"
print(a1+a2)